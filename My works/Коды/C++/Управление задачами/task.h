#ifndef TASK_H
#define TASK_H

#include <QString>

class Task
{
public:
    Task(const QString &description);

    QString getDescription() const;

private:
    QString description;
};

#endif // TASK_H