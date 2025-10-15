---
theme:
  path: theme.yaml
  override:
    default:
      margin:
        percent: 8

title: learn linux
sub_title: and why you should care
author: Kyle Trinh
---

<!-- font_size: 1 -->
whoami
===

<!-- column_layout: [2, 2] -->

<!-- column: 0 -->

# main
* 4th year, computer science + mathematics
* sacramento, ca

## job
* operating systems intern @ ServiceNow
* swe intern @ Insulet Corporation
* research @ Kale Research Group
* research @ UCSD Computational Number Theory
* research / swe @ Center for Applied Internet Data Analysis

### links
* github.com/pink10000
  * source code / pdf available at the end
* linkedin.com/in/kytrinh
* kytrinh.me


#### acknolwedgements

built with 
- `presenterm` (slides) 
- `kitty` (presentation medium)
- color scheme: ibm oxocarbon base-16
- font: berkeley mono

<!-- column: 1 -->

![image:width:70%](./assets/scale.jpg)

<!-- alignment: center -->
 pasadena, california

<!-- end_slide -->

what is an operating system?
===
<!-- 
  speaker_note: |
  An operating system is a collection of software that manages a computer's hardware and applications by allocating resources. 
 -->

<!-- new_lines: 4 -->
<!-- font_size: 3 -->
> An operating system is a collection of software that manages a computer's hardware and applications by allocating resources. 

<!-- end_slide -->


pronounciation
===
<!-- column_layout: [3, 1] -->
<!-- column: 0 -->
<!-- new_lines: 4 -->

```bash +exec
curl https://upload.wikimedia.org/wikipedia/commons/0/03/Linus-linux.ogg | ffplay -v 0 -nodisp -autoexit -
```

<!-- column: 1 -->
<!-- new_lines: 7 -->
![](./assets/tux.png)

<!-- reset_layout -->
*Did you know?*

Linux Torvalds announced in 1996 that there would be a mascot for Linux, a penguin. This was because when they were about to select the mascot, Torvalds mentioned he was bitten by a little penguin (Eudyptula minor) on a visit to the National Zoo & Aquarium in Canberra, Australia. It's name is `Tux`.

Source: `https://archive.org/details/justforfun00linu/page/84/mode/2up` 

<!-- end_slide -->

<!-- jump_to_middle -->
brief history 
===
<!-- end_slide -->


<!-- 
  speaker_note: |
  Ken Thompson, Dennis Ritchie, and others at Bell Labs begin development on UNIX. It establishes many core concepts like the command-line interface, hierarchical file system, and the "everything is a file" philosophy that Linux would later adopt.
 -->
<!-- font_size: 2 -->
# 1969: UNIX 
![image:width:60%](./assets/Ken_Thompson_and_Dennis_Ritchie.jpg)
<!-- alignment: center -->
Ken Thompson & Dennis Ritchie

<!-- end_slide -->


<!-- 
  speaker_note: |
  Richard Stallman launches the GNU Project with the goal of creating a completely free and open-source UNIX-like operating system. He and others create essential tools like the GCC compiler and the Bash shell, but they lack a kernel.
-->
<!-- font_size: 2 -->
# 1983: GNU Project

<!-- end_slide -->


<!-- 
  speaker_note: |
  Linus Torvalds, a student in Finland, posts a now-famous message to a newsgroup announcing his new hobby project: a free operating system kernel.
-->
<!-- font_size: 2 -->
# 1991: Linus Torvalds

<!-- end_slide -->

<!-- 
  speaker_note: |
  The Linux kernel is licensed under the GNU General Public License (GPL). This is a critical moment. It allows developers to legally combine the GNU project's tools with the Linux kernel to create a complete, free operating system, often called GNU/Linux.
 -->
<!-- font_size: 2 -->
# 1992: GNU/Linux

<!-- end_slide -->


<!-- 
  speaker_note: | 
  The first major Linux distributions, like Slackware, Debian, Red Hat Linux are created. These packages bundle the kernel with software and a package manager, making Linux accessible to a wider audience. -->
<!-- font_size: 2 -->
# 1993-1997: Major Linux Distributions

<!-- end_slide -->


<!-- 
  speaker_note: |
  Commerical companies began selling and supporting Linux distributions
  For example, 
  - 1999: IBM joined forces with Red Hat, announcing support for Linux
  - 1999: Dell began pre-installing Linux on select servers
  - 2000: The GNOME and KDE desktop environments evolved, making Linux more user friendly for desktop users.
  - 2000: IBM invested $1 billion in Linux development.
  This, combined with the rise of the internet, led to Linux becoming the backbone of the dot-com boom and powered web servers around the world.
-->
<!-- font_size: 2 -->
# 1998-2000: Commercial Linux

<!-- end_slide -->

<!-- 
  speaker_note: |
  Google launches Android, an operating system for mobile devices built on top of the Linux kernel. This puts Linux into the hands of billions of users globally.
 -->
<!-- font_size: 2 -->
# 2007: Android


<!-- end_slide -->

<!-- 
  speaker_note: |
  Today, linux completely dominates cloud computing, super computing, and IoT devices. It runs on the vast majority of the world's servers and is even integrated with Microsoft via the Windows Subsystem for Linux (WSL).
 -->
<!-- font_size: 2 -->
# Today: Ubiquity


<!-- end_slide -->


<!-- font_size: 2 -->
# why linux? 




<!-- end_slide -->
cd (cli fundamentals)
===

<!-- end_slide -->
apt/pacman/brew (package management)
===

<!-- end_slide -->
ping (basic networking)
===

<!-- end_slide -->
lscpu (high performance computing)
===

<!-- end_slide -->
nix-shell (reproducible environments)
===

<!-- end_slide -->
(git) linux @ a job
===

<!-- end_slide -->
conclusion
===

<!-- end_slide -->
q&a
===

<!-- end_slide -->