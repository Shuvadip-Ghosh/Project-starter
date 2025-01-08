## Streamline Your Development Workflow: Introducing the GitHub Automator

This innovative project automates the initial setup process for your coding endeavors, saving you valuable time and effort.  Built specifically for Windows users, the GitHub Automator eliminates the repetitive tasks associated with project initiation, allowing you to seamlessly transition from project conception to coding implementation.

**Enhanced Efficiency for Novice Programmers**

* **Effortless Project Kickoff:** Eliminate the tedious manual steps of creating folders, initializing Git repositories, crafting README files, and establishing connections on GitHub. This tool automates these steps, propelling you directly into the coding phase with minimal setup time.
* **Immediate Coding Focus:** With a single command, you'll have your project environment primed and ready, empowering you to channel your energy into the heart of development – writing code.

**Elevate Your Development Workflow: Embrace the "Cool Programmer" Approach**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Shuvadip-Ghosh/Project-starter.git
   ```

2. **Configure `start.py`:**

   - Locate the `start.py` file within the cloned repository.
   - For enhanced usability, consider adding the path to `start.py` to your system's environment variables, enabling execution from any directory.

**Command-Line Powerhouse: Streamlined Project Initiation**

The script leverages the following syntax for maximum control:

```bash
python start.py -n <repo-name> -d "<description-for-repo>" [options]
```

**Decoding the Available Options:**

* `-pr`: Make your remote repository private on GitHub (optional).

```bash
python start.py -n <repo-name> -d <description-for-repo> -pr
```

* `-upd`: For advanced users, this flag allows updating the default directory for new repositories and the preferred browser for authentication (interactive process).

```bash
python start.py -upd
```

**Supported Browsers:**

* Microsoft Edge
* Google Chrome
* Mozilla Firefox

**Essential Considerations for Optimal Performance:**

- **Prerequisites:** Ensure both Git and Python are installed on your system and you are signed in to your github account in the browser you are about to specify and you know the details you are going to be needed during the first time setup before running the script.
- **Potential for Personalization:** While the script automates the fundamental setup, there's room for further customization to suit your workflow. You could potentially integrate tasks like installing project dependencies or setting up a virtual environment for even greater automation.


By incorporating the GitHub Automator into your development process, you'll experience a significantly streamlined and efficient project setup, allowing you to dedicate more time and focus to the core aspects of software development – creating innovative and impactful code.
