#include "mainwindow.h"
#include <QVBoxLayout>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    // Создаем основной виджет и задаем ему вертикальный layout
    QWidget *centralWidget = new QWidget(this);
    QVBoxLayout *layout = new QVBoxLayout(centralWidget);

    // Создаем элементы интерфейса
    taskList = new QListWidget(this);
    taskInput = new QLineEdit(this);
    addTaskButton = new QPushButton("Добавить задачу", this);
    removeTaskButton = new QPushButton("Удалить задачу", this);

    // Добавляем элементы на layout
    layout->addWidget(taskList);
    layout->addWidget(taskInput);
    layout->addWidget(addTaskButton);
    layout->addWidget(removeTaskButton);

    // Устанавливаем центральный виджет
    setCentralWidget(centralWidget);

    // Соединяем сигналы и слоты
    connect(addTaskButton, &QPushButton::clicked, this, &MainWindow::addTask);
    connect(removeTaskButton, &QPushButton::clicked, this, &MainWindow::removeTask);
}

MainWindow::~MainWindow() {}

void MainWindow::addTask() {
    QString taskDescription = taskInput->text();
    if (!taskDescription.isEmpty()) {
        Task newTask(taskDescription);
        taskList->addItem(newTask.getDescription());
        taskInput->clear();
    }
}

void MainWindow::removeTask() {
    QListWidgetItem *item = taskList->currentItem();
    if (item) {
        delete item;
    }
}