#include "task.h"

Task::Task(const QString &description) : description(description) {}

QString Task::getDescription() const {
    return description;
}