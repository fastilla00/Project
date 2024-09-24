#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QListWidget>
#include <QPushButton>
#include <QLineEdit>
#include "task.h"

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void addTask();
    void removeTask();

private:
    QListWidget *taskList;
    QLineEdit *taskInput;
    QPushButton *addTaskButton;
    QPushButton *removeTaskButton;
};

#endif // MAINWINDOW_H