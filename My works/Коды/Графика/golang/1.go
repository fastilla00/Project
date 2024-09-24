package main

import (
	"image/color"
	"log"
	"os"

	"github.com/go-audio/wav"
	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/ebitenutil"
)

// Размеры экрана
const screenWidth = 640
const screenHeight = 480

// AudioVisualizer - структура для визуализатора
type AudioVisualizer struct {
	audioData    []int
	position     int
	volume       float64
	reversed     bool
	trimStartPos int // Начальная позиция для обрезки
	trimEndPos   int // Конечная позиция для обрезки
	isTrimming   bool
}

// LoadWavFile - функция для загрузки и декодирования WAV файла
func LoadWavFile(fileName string) ([]int, error) {
	// Открытие файла
	f, err := os.Open(fileName)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	// Декодирование WAV файла
	wavDecoder := wav.NewDecoder(f)
	buf, err := wavDecoder.FullPCMBuffer()
	if err != nil {
		return nil, err
	}

	// Преобразование данных в int массив для визуализации
	audioData := make([]int, buf.NumFrames())
	for i := 0; i < buf.NumFrames(); i++ {
		audioData[i] = int(buf.Data[i])
	}
	return audioData, nil
}

// ReverseAudio - функция для реверса аудиодорожки
func (av *AudioVisualizer) ReverseAudio() {
	for i, j := 0, len(av.audioData)-1; i < j; i, j = i+1, j-1 {
		av.audioData[i], av.audioData[j] = av.audioData[j], av.audioData[i]
	}
	av.reversed = !av.reversed
}

// AdjustVolume - функция для изменения громкости
func (av *AudioVisualizer) AdjustVolume(factor float64) {
	av.volume *= factor
	for i := range av.audioData {
		av.audioData[i] = int(float64(av.audioData[i]) * av.volume)
	}
}

// TrimAudio - функция для обрезки аудиодорожки
func (av *AudioVisualizer) TrimAudio() {
	if av.trimEndPos > av.trimStartPos {
		av.audioData = av.audioData[av.trimStartPos:av.trimEndPos]
		av.position = 0 // Обнуляем позицию, чтобы начать с начала новой обрезанной дорожки
	}
}

// Update - обновляет позицию визуализации и обрабатывает ввод
func (av *AudioVisualizer) Update() error {
	// Управление звуком
	if ebiten.IsKeyPressed(ebiten.KeyUp) {
		av.AdjustVolume(1.1) // Увеличение громкости
	}
	if ebiten.IsKeyPressed(ebiten.KeyDown) {
		av.AdjustVolume(0.9) // Уменьшение громкости
	}

	// Реверс аудио при нажатии на R
	if ebiten.IsKeyPressed(ebiten.KeyR) && !av.reversed {
		av.ReverseAudio()
	}

	// Начало обрезки при нажатии на клавишу S
	if ebiten.IsKeyPressed(ebiten.KeyS) && !av.isTrimming {
		av.trimStartPos = av.position
		av.isTrimming = true
	}

	// Конец обрезки при нажатии на клавишу E
	if ebiten.IsKeyPressed(ebiten.KeyE) && av.isTrimming {
		av.trimEndPos = av.position
		av.TrimAudio() // Выполняем обрезку
		av.isTrimming = false
	}

	// Прокрутка аудиоданных
	av.position += 500 // Количество шагов для прокрутки
	if av.position >= len(av.audioData) {
		av.position = 0
	}
	return nil
}

// Draw - отрисовка визуализации на экране
func (av *AudioVisualizer) Draw(screen *ebiten.Image) {
	screen.Fill(color.Black)

	// Рисуем звуковые волны
	for x := 0; x < screenWidth; x++ {
		index := (av.position + x) % len(av.audioData)
		y := screenHeight/2 + av.audioData[index]/100 // Масштабируем амплитуду
		ebitenutil.DrawLine(screen, float64(x), float64(screenHeight/2), float64(x), float64(y), color.White)
	}
}

// Layout - задает размеры экрана
func (av *AudioVisualizer) Layout(outsideWidth, outsideHeight int) (int, int) {
	return screenWidth, screenHeight
}

func main() {
	// Загружаем аудиофайл
	audioData, err := LoadWavFile("sample.wav")
	if err != nil {
		log.Fatal("Ошибка при загрузке WAV файла:", err)
	}

	// Создаем визуализатор с начальными параметрами
	visualizer := &AudioVisualizer{
		audioData:    audioData,
		position:     0,
		volume:       1.0, // Начальный уровень громкости
		reversed:     false,
		trimStartPos: 0,
		trimEndPos:   len(audioData),
		isTrimming:   false,
	}

	// Запускаем визуализатор
	ebiten.SetWindowSize(screenWidth, screenHeight)
	ebiten.SetWindowTitle("Audio Visualizer with Editing and Trimming")
	if err := ebiten.RunGame(visualizer); err != nil {
		log.Fatal(err)
	}
}
