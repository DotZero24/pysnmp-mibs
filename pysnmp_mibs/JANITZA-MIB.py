_F='Integer32'
_E='sysUpTime'
_D='read-only'
_C='current'
_B='mandatory'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysUpTime,=mibBuilder.importSymbols('SNMPv2-MIB',_E)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,2,1,1))
_SysDescr_Type=OctetString
_SysDescr_Object=MibScalar
sysDescr=_SysDescr_Object((1,3,6,1,2,1,1,1),_SysDescr_Type())
sysDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDescr.setStatus(_C)
_SysObjectID_Type=ObjectIdentifier
_SysObjectID_Object=MibScalar
sysObjectID=_SysObjectID_Object((1,3,6,1,2,1,1,2),_SysObjectID_Type())
sysObjectID.setMaxAccess(_D)
if mibBuilder.loadTexts:sysObjectID.setStatus(_C)
_SysUpTime_Type=TimeTicks
_SysUpTime_Object=MibScalar
sysUpTime=_SysUpTime_Object((1,3,6,1,2,1,1,3),_SysUpTime_Type())
sysUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sysUpTime.setStatus(_C)
_SysName_Type=OctetString
_SysName_Object=MibScalar
sysName=_SysName_Object((1,3,6,1,2,1,1,5),_SysName_Type())
sysName.setMaxAccess(_A)
if mibBuilder.loadTexts:sysName.setStatus(_C)
_SysLocation_Type=OctetString
_SysLocation_Object=MibScalar
sysLocation=_SysLocation_Object((1,3,6,1,2,1,1,6),_SysLocation_Type())
sysLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:sysLocation.setStatus(_C)
class _SysServices_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_SysServices_Type.__name__=_F
_SysServices_Object=MibScalar
sysServices=_SysServices_Object((1,3,6,1,2,1,1,7),_SysServices_Type())
sysServices.setMaxAccess(_D)
if mibBuilder.loadTexts:sysServices.setStatus(_C)
_Snmp_ObjectIdentity=ObjectIdentity
snmp=_Snmp_ObjectIdentity((1,3,6,1,2,1,11))
_Janitza_ObjectIdentity=ObjectIdentity
janitza=_Janitza_ObjectIdentity((1,3,6,1,4,1,34278))
_RmsPhase_ObjectIdentity=ObjectIdentity
rmsPhase=_RmsPhase_ObjectIdentity((1,3,6,1,4,1,34278,1))
_ULN1_Type=Integer32
_ULN1_Object=MibScalar
uLN1=_ULN1_Object((1,3,6,1,4,1,34278,1,1),_ULN1_Type())
uLN1.setMaxAccess(_A)
if mibBuilder.loadTexts:uLN1.setStatus(_B)
_ULN2_Type=Integer32
_ULN2_Object=MibScalar
uLN2=_ULN2_Object((1,3,6,1,4,1,34278,1,2),_ULN2_Type())
uLN2.setMaxAccess(_A)
if mibBuilder.loadTexts:uLN2.setStatus(_B)
_ULN3_Type=Integer32
_ULN3_Object=MibScalar
uLN3=_ULN3_Object((1,3,6,1,4,1,34278,1,3),_ULN3_Type())
uLN3.setMaxAccess(_A)
if mibBuilder.loadTexts:uLN3.setStatus(_B)
_ULN4_Type=Integer32
_ULN4_Object=MibScalar
uLN4=_ULN4_Object((1,3,6,1,4,1,34278,1,4),_ULN4_Type())
uLN4.setMaxAccess(_A)
if mibBuilder.loadTexts:uLN4.setStatus(_B)
_UL1L2_Type=Integer32
_UL1L2_Object=MibScalar
uL1L2=_UL1L2_Object((1,3,6,1,4,1,34278,1,5),_UL1L2_Type())
uL1L2.setMaxAccess(_A)
if mibBuilder.loadTexts:uL1L2.setStatus(_B)
_UL2L3_Type=Integer32
_UL2L3_Object=MibScalar
uL2L3=_UL2L3_Object((1,3,6,1,4,1,34278,1,6),_UL2L3_Type())
uL2L3.setMaxAccess(_A)
if mibBuilder.loadTexts:uL2L3.setStatus(_B)
_UL3L1_Type=Integer32
_UL3L1_Object=MibScalar
uL3L1=_UL3L1_Object((1,3,6,1,4,1,34278,1,7),_UL3L1_Type())
uL3L1.setMaxAccess(_A)
if mibBuilder.loadTexts:uL3L1.setStatus(_B)
_IL1_Type=Integer32
_IL1_Object=MibScalar
iL1=_IL1_Object((1,3,6,1,4,1,34278,1,8),_IL1_Type())
iL1.setMaxAccess(_A)
if mibBuilder.loadTexts:iL1.setStatus(_B)
_IL2_Type=Integer32
_IL2_Object=MibScalar
iL2=_IL2_Object((1,3,6,1,4,1,34278,1,9),_IL2_Type())
iL2.setMaxAccess(_A)
if mibBuilder.loadTexts:iL2.setStatus(_B)
_IL3_Type=Integer32
_IL3_Object=MibScalar
iL3=_IL3_Object((1,3,6,1,4,1,34278,1,10),_IL3_Type())
iL3.setMaxAccess(_A)
if mibBuilder.loadTexts:iL3.setStatus(_B)
_IL4_Type=Integer32
_IL4_Object=MibScalar
iL4=_IL4_Object((1,3,6,1,4,1,34278,1,11),_IL4_Type())
iL4.setMaxAccess(_A)
if mibBuilder.loadTexts:iL4.setStatus(_B)
_PL1_Type=Integer32
_PL1_Object=MibScalar
pL1=_PL1_Object((1,3,6,1,4,1,34278,1,12),_PL1_Type())
pL1.setMaxAccess(_A)
if mibBuilder.loadTexts:pL1.setStatus(_B)
_PL2_Type=Integer32
_PL2_Object=MibScalar
pL2=_PL2_Object((1,3,6,1,4,1,34278,1,13),_PL2_Type())
pL2.setMaxAccess(_A)
if mibBuilder.loadTexts:pL2.setStatus(_B)
_PL3_Type=Integer32
_PL3_Object=MibScalar
pL3=_PL3_Object((1,3,6,1,4,1,34278,1,14),_PL3_Type())
pL3.setMaxAccess(_A)
if mibBuilder.loadTexts:pL3.setStatus(_B)
_PL4_Type=Integer32
_PL4_Object=MibScalar
pL4=_PL4_Object((1,3,6,1,4,1,34278,1,15),_PL4_Type())
pL4.setMaxAccess(_A)
if mibBuilder.loadTexts:pL4.setStatus(_B)
_QL1_Type=Integer32
_QL1_Object=MibScalar
qL1=_QL1_Object((1,3,6,1,4,1,34278,1,16),_QL1_Type())
qL1.setMaxAccess(_A)
if mibBuilder.loadTexts:qL1.setStatus(_B)
_QL2_Type=Integer32
_QL2_Object=MibScalar
qL2=_QL2_Object((1,3,6,1,4,1,34278,1,17),_QL2_Type())
qL2.setMaxAccess(_A)
if mibBuilder.loadTexts:qL2.setStatus(_B)
_QL3_Type=Integer32
_QL3_Object=MibScalar
qL3=_QL3_Object((1,3,6,1,4,1,34278,1,18),_QL3_Type())
qL3.setMaxAccess(_A)
if mibBuilder.loadTexts:qL3.setStatus(_B)
_QL4_Type=Integer32
_QL4_Object=MibScalar
qL4=_QL4_Object((1,3,6,1,4,1,34278,1,19),_QL4_Type())
qL4.setMaxAccess(_A)
if mibBuilder.loadTexts:qL4.setStatus(_B)
_SL1_Type=Integer32
_SL1_Object=MibScalar
sL1=_SL1_Object((1,3,6,1,4,1,34278,1,20),_SL1_Type())
sL1.setMaxAccess(_A)
if mibBuilder.loadTexts:sL1.setStatus(_B)
_SL2_Type=Integer32
_SL2_Object=MibScalar
sL2=_SL2_Object((1,3,6,1,4,1,34278,1,21),_SL2_Type())
sL2.setMaxAccess(_A)
if mibBuilder.loadTexts:sL2.setStatus(_B)
_SL3_Type=Integer32
_SL3_Object=MibScalar
sL3=_SL3_Object((1,3,6,1,4,1,34278,1,22),_SL3_Type())
sL3.setMaxAccess(_A)
if mibBuilder.loadTexts:sL3.setStatus(_B)
_SL4_Type=Integer32
_SL4_Object=MibScalar
sL4=_SL4_Object((1,3,6,1,4,1,34278,1,23),_SL4_Type())
sL4.setMaxAccess(_A)
if mibBuilder.loadTexts:sL4.setStatus(_B)
_CosPL1_Type=Integer32
_CosPL1_Object=MibScalar
cosPL1=_CosPL1_Object((1,3,6,1,4,1,34278,1,24),_CosPL1_Type())
cosPL1.setMaxAccess(_A)
if mibBuilder.loadTexts:cosPL1.setStatus(_B)
_CosPL2_Type=Integer32
_CosPL2_Object=MibScalar
cosPL2=_CosPL2_Object((1,3,6,1,4,1,34278,1,25),_CosPL2_Type())
cosPL2.setMaxAccess(_A)
if mibBuilder.loadTexts:cosPL2.setStatus(_B)
_CosPL3_Type=Integer32
_CosPL3_Object=MibScalar
cosPL3=_CosPL3_Object((1,3,6,1,4,1,34278,1,26),_CosPL3_Type())
cosPL3.setMaxAccess(_A)
if mibBuilder.loadTexts:cosPL3.setStatus(_B)
_CosPL4_Type=Integer32
_CosPL4_Object=MibScalar
cosPL4=_CosPL4_Object((1,3,6,1,4,1,34278,1,27),_CosPL4_Type())
cosPL4.setMaxAccess(_A)
if mibBuilder.loadTexts:cosPL4.setStatus(_B)
_RmsSumme3_ObjectIdentity=ObjectIdentity
rmsSumme3=_RmsSumme3_ObjectIdentity((1,3,6,1,4,1,34278,2))
_P3_Type=Integer32
_P3_Object=MibScalar
p3=_P3_Object((1,3,6,1,4,1,34278,2,1),_P3_Type())
p3.setMaxAccess(_A)
if mibBuilder.loadTexts:p3.setStatus(_B)
_Q3_Type=Integer32
_Q3_Object=MibScalar
q3=_Q3_Object((1,3,6,1,4,1,34278,2,2),_Q3_Type())
q3.setMaxAccess(_A)
if mibBuilder.loadTexts:q3.setStatus(_B)
_S3_Type=Integer32
_S3_Object=MibScalar
s3=_S3_Object((1,3,6,1,4,1,34278,2,3),_S3_Type())
s3.setMaxAccess(_A)
if mibBuilder.loadTexts:s3.setStatus(_B)
_CosP3_Type=Integer32
_CosP3_Object=MibScalar
cosP3=_CosP3_Object((1,3,6,1,4,1,34278,2,4),_CosP3_Type())
cosP3.setMaxAccess(_A)
if mibBuilder.loadTexts:cosP3.setStatus(_B)
_RmsSumme4_ObjectIdentity=ObjectIdentity
rmsSumme4=_RmsSumme4_ObjectIdentity((1,3,6,1,4,1,34278,3))
_P4_Type=Integer32
_P4_Object=MibScalar
p4=_P4_Object((1,3,6,1,4,1,34278,3,1),_P4_Type())
p4.setMaxAccess(_A)
if mibBuilder.loadTexts:p4.setStatus(_B)
_Q4_Type=Integer32
_Q4_Object=MibScalar
q4=_Q4_Object((1,3,6,1,4,1,34278,3,2),_Q4_Type())
q4.setMaxAccess(_A)
if mibBuilder.loadTexts:q4.setStatus(_B)
_S4_Type=Integer32
_S4_Object=MibScalar
s4=_S4_Object((1,3,6,1,4,1,34278,3,3),_S4_Type())
s4.setMaxAccess(_A)
if mibBuilder.loadTexts:s4.setStatus(_B)
_CosP4_Type=Integer32
_CosP4_Object=MibScalar
cosP4=_CosP4_Object((1,3,6,1,4,1,34278,3,4),_CosP4_Type())
cosP4.setMaxAccess(_A)
if mibBuilder.loadTexts:cosP4.setStatus(_B)
_EnergiePhase_ObjectIdentity=ObjectIdentity
energiePhase=_EnergiePhase_ObjectIdentity((1,3,6,1,4,1,34278,4))
_WhL1_Type=Integer32
_WhL1_Object=MibScalar
whL1=_WhL1_Object((1,3,6,1,4,1,34278,4,1),_WhL1_Type())
whL1.setMaxAccess(_A)
if mibBuilder.loadTexts:whL1.setStatus(_B)
_WhL2_Type=Integer32
_WhL2_Object=MibScalar
whL2=_WhL2_Object((1,3,6,1,4,1,34278,4,2),_WhL2_Type())
whL2.setMaxAccess(_A)
if mibBuilder.loadTexts:whL2.setStatus(_B)
_WhL3_Type=Integer32
_WhL3_Object=MibScalar
whL3=_WhL3_Object((1,3,6,1,4,1,34278,4,3),_WhL3_Type())
whL3.setMaxAccess(_A)
if mibBuilder.loadTexts:whL3.setStatus(_B)
_WhL4_Type=Integer32
_WhL4_Object=MibScalar
whL4=_WhL4_Object((1,3,6,1,4,1,34278,4,4),_WhL4_Type())
whL4.setMaxAccess(_A)
if mibBuilder.loadTexts:whL4.setStatus(_B)
_QhL1_Type=Integer32
_QhL1_Object=MibScalar
qhL1=_QhL1_Object((1,3,6,1,4,1,34278,4,5),_QhL1_Type())
qhL1.setMaxAccess(_A)
if mibBuilder.loadTexts:qhL1.setStatus(_B)
_QhL2_Type=Integer32
_QhL2_Object=MibScalar
qhL2=_QhL2_Object((1,3,6,1,4,1,34278,4,6),_QhL2_Type())
qhL2.setMaxAccess(_A)
if mibBuilder.loadTexts:qhL2.setStatus(_B)
_QhL3_Type=Integer32
_QhL3_Object=MibScalar
qhL3=_QhL3_Object((1,3,6,1,4,1,34278,4,7),_QhL3_Type())
qhL3.setMaxAccess(_A)
if mibBuilder.loadTexts:qhL3.setStatus(_B)
_QhL4_Type=Integer32
_QhL4_Object=MibScalar
qhL4=_QhL4_Object((1,3,6,1,4,1,34278,4,8),_QhL4_Type())
qhL4.setMaxAccess(_A)
if mibBuilder.loadTexts:qhL4.setStatus(_B)
_EnergieSumme3_ObjectIdentity=ObjectIdentity
energieSumme3=_EnergieSumme3_ObjectIdentity((1,3,6,1,4,1,34278,5))
_Wh3_Type=Integer32
_Wh3_Object=MibScalar
wh3=_Wh3_Object((1,3,6,1,4,1,34278,5,1),_Wh3_Type())
wh3.setMaxAccess(_A)
if mibBuilder.loadTexts:wh3.setStatus(_B)
_Qh3_Type=Integer32
_Qh3_Object=MibScalar
qh3=_Qh3_Object((1,3,6,1,4,1,34278,5,2),_Qh3_Type())
qh3.setMaxAccess(_A)
if mibBuilder.loadTexts:qh3.setStatus(_B)
_EnergieSumme4_ObjectIdentity=ObjectIdentity
energieSumme4=_EnergieSumme4_ObjectIdentity((1,3,6,1,4,1,34278,6))
_Wh4_Type=Integer32
_Wh4_Object=MibScalar
wh4=_Wh4_Object((1,3,6,1,4,1,34278,6,1),_Wh4_Type())
wh4.setMaxAccess(_A)
if mibBuilder.loadTexts:wh4.setStatus(_B)
_Qh4_Type=Integer32
_Qh4_Object=MibScalar
qh4=_Qh4_Object((1,3,6,1,4,1,34278,6,2),_Qh4_Type())
qh4.setMaxAccess(_A)
if mibBuilder.loadTexts:qh4.setStatus(_B)
_Thd_ObjectIdentity=ObjectIdentity
thd=_Thd_ObjectIdentity((1,3,6,1,4,1,34278,7))
_ThdULN1_Type=Integer32
_ThdULN1_Object=MibScalar
thdULN1=_ThdULN1_Object((1,3,6,1,4,1,34278,7,1),_ThdULN1_Type())
thdULN1.setMaxAccess(_A)
if mibBuilder.loadTexts:thdULN1.setStatus(_B)
_ThdULN2_Type=Integer32
_ThdULN2_Object=MibScalar
thdULN2=_ThdULN2_Object((1,3,6,1,4,1,34278,7,2),_ThdULN2_Type())
thdULN2.setMaxAccess(_A)
if mibBuilder.loadTexts:thdULN2.setStatus(_B)
_ThdULN3_Type=Integer32
_ThdULN3_Object=MibScalar
thdULN3=_ThdULN3_Object((1,3,6,1,4,1,34278,7,3),_ThdULN3_Type())
thdULN3.setMaxAccess(_A)
if mibBuilder.loadTexts:thdULN3.setStatus(_B)
_ThdULN4_Type=Integer32
_ThdULN4_Object=MibScalar
thdULN4=_ThdULN4_Object((1,3,6,1,4,1,34278,7,4),_ThdULN4_Type())
thdULN4.setMaxAccess(_A)
if mibBuilder.loadTexts:thdULN4.setStatus(_B)
_ThdIL1_Type=Integer32
_ThdIL1_Object=MibScalar
thdIL1=_ThdIL1_Object((1,3,6,1,4,1,34278,7,5),_ThdIL1_Type())
thdIL1.setMaxAccess(_A)
if mibBuilder.loadTexts:thdIL1.setStatus(_B)
_ThdIL2_Type=Integer32
_ThdIL2_Object=MibScalar
thdIL2=_ThdIL2_Object((1,3,6,1,4,1,34278,7,6),_ThdIL2_Type())
thdIL2.setMaxAccess(_A)
if mibBuilder.loadTexts:thdIL2.setStatus(_B)
_ThdIL3_Type=Integer32
_ThdIL3_Object=MibScalar
thdIL3=_ThdIL3_Object((1,3,6,1,4,1,34278,7,7),_ThdIL3_Type())
thdIL3.setMaxAccess(_A)
if mibBuilder.loadTexts:thdIL3.setStatus(_B)
_ThdIL4_Type=Integer32
_ThdIL4_Object=MibScalar
thdIL4=_ThdIL4_Object((1,3,6,1,4,1,34278,7,8),_ThdIL4_Type())
thdIL4.setMaxAccess(_A)
if mibBuilder.loadTexts:thdIL4.setStatus(_B)
_Misc_ObjectIdentity=ObjectIdentity
misc=_Misc_ObjectIdentity((1,3,6,1,4,1,34278,8))
_Frequenz_Type=Integer32
_Frequenz_Object=MibScalar
frequenz=_Frequenz_Object((1,3,6,1,4,1,34278,8,1),_Frequenz_Type())
frequenz.setMaxAccess(_A)
if mibBuilder.loadTexts:frequenz.setStatus(_B)
_User_ObjectIdentity=ObjectIdentity
user=_User_ObjectIdentity((1,3,6,1,4,1,34278,9))
_JasicVAR1_Type=Integer32
_JasicVAR1_Object=MibScalar
jasicVAR1=_JasicVAR1_Object((1,3,6,1,4,1,34278,9,1),_JasicVAR1_Type())
jasicVAR1.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR1.setStatus(_B)
_JasicVAR2_Type=Integer32
_JasicVAR2_Object=MibScalar
jasicVAR2=_JasicVAR2_Object((1,3,6,1,4,1,34278,9,2),_JasicVAR2_Type())
jasicVAR2.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR2.setStatus(_B)
_JasicVAR3_Type=Integer32
_JasicVAR3_Object=MibScalar
jasicVAR3=_JasicVAR3_Object((1,3,6,1,4,1,34278,9,3),_JasicVAR3_Type())
jasicVAR3.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR3.setStatus(_B)
_JasicVAR4_Type=Integer32
_JasicVAR4_Object=MibScalar
jasicVAR4=_JasicVAR4_Object((1,3,6,1,4,1,34278,9,4),_JasicVAR4_Type())
jasicVAR4.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR4.setStatus(_B)
_JasicVAR5_Type=Integer32
_JasicVAR5_Object=MibScalar
jasicVAR5=_JasicVAR5_Object((1,3,6,1,4,1,34278,9,5),_JasicVAR5_Type())
jasicVAR5.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR5.setStatus(_B)
_JasicVAR6_Type=Integer32
_JasicVAR6_Object=MibScalar
jasicVAR6=_JasicVAR6_Object((1,3,6,1,4,1,34278,9,6),_JasicVAR6_Type())
jasicVAR6.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR6.setStatus(_B)
_JasicVAR7_Type=Integer32
_JasicVAR7_Object=MibScalar
jasicVAR7=_JasicVAR7_Object((1,3,6,1,4,1,34278,9,7),_JasicVAR7_Type())
jasicVAR7.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR7.setStatus(_B)
_JasicVAR8_Type=Integer32
_JasicVAR8_Object=MibScalar
jasicVAR8=_JasicVAR8_Object((1,3,6,1,4,1,34278,9,8),_JasicVAR8_Type())
jasicVAR8.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR8.setStatus(_B)
_JasicVAR9_Type=Integer32
_JasicVAR9_Object=MibScalar
jasicVAR9=_JasicVAR9_Object((1,3,6,1,4,1,34278,9,9),_JasicVAR9_Type())
jasicVAR9.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR9.setStatus(_B)
_JasicVAR10_Type=Integer32
_JasicVAR10_Object=MibScalar
jasicVAR10=_JasicVAR10_Object((1,3,6,1,4,1,34278,9,10),_JasicVAR10_Type())
jasicVAR10.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR10.setStatus(_B)
_JasicVAR11_Type=Integer32
_JasicVAR11_Object=MibScalar
jasicVAR11=_JasicVAR11_Object((1,3,6,1,4,1,34278,9,11),_JasicVAR11_Type())
jasicVAR11.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR11.setStatus(_B)
_JasicVAR12_Type=Integer32
_JasicVAR12_Object=MibScalar
jasicVAR12=_JasicVAR12_Object((1,3,6,1,4,1,34278,9,12),_JasicVAR12_Type())
jasicVAR12.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR12.setStatus(_B)
_JasicVAR13_Type=Integer32
_JasicVAR13_Object=MibScalar
jasicVAR13=_JasicVAR13_Object((1,3,6,1,4,1,34278,9,13),_JasicVAR13_Type())
jasicVAR13.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR13.setStatus(_B)
_JasicVAR14_Type=Integer32
_JasicVAR14_Object=MibScalar
jasicVAR14=_JasicVAR14_Object((1,3,6,1,4,1,34278,9,14),_JasicVAR14_Type())
jasicVAR14.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR14.setStatus(_B)
_JasicVAR15_Type=Integer32
_JasicVAR15_Object=MibScalar
jasicVAR15=_JasicVAR15_Object((1,3,6,1,4,1,34278,9,15),_JasicVAR15_Type())
jasicVAR15.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR15.setStatus(_B)
_JasicVAR16_Type=Integer32
_JasicVAR16_Object=MibScalar
jasicVAR16=_JasicVAR16_Object((1,3,6,1,4,1,34278,9,16),_JasicVAR16_Type())
jasicVAR16.setMaxAccess(_A)
if mibBuilder.loadTexts:jasicVAR16.setStatus(_B)
coldStart=NotificationType((1,3,6,1,2,1,11,0,0))
if mibBuilder.loadTexts:coldStart.setStatus('')
warmStart=NotificationType((1,3,6,1,2,1,11,0,1))
if mibBuilder.loadTexts:warmStart.setStatus('')
userTrap1=NotificationType((1,3,6,1,4,1,34278,0,6))
if mibBuilder.loadTexts:userTrap1.setStatus('')
userTrap2=NotificationType((1,3,6,1,4,1,34278,0,7))
if mibBuilder.loadTexts:userTrap2.setStatus('')
userTrap3=NotificationType((1,3,6,1,4,1,34278,0,8))
if mibBuilder.loadTexts:userTrap3.setStatus('')
userTrap4=NotificationType((1,3,6,1,4,1,34278,0,9))
if mibBuilder.loadTexts:userTrap4.setStatus('')
userTrap5=NotificationType((1,3,6,1,4,1,34278,0,10))
if mibBuilder.loadTexts:userTrap5.setStatus('')
userTrap6=NotificationType((1,3,6,1,4,1,34278,0,11))
if mibBuilder.loadTexts:userTrap6.setStatus('')
userTrap7=NotificationType((1,3,6,1,4,1,34278,0,12))
if mibBuilder.loadTexts:userTrap7.setStatus('')
userTrap8=NotificationType((1,3,6,1,4,1,34278,0,13))
if mibBuilder.loadTexts:userTrap8.setStatus('')
userTrap9=NotificationType((1,3,6,1,4,1,34278,0,14))
if mibBuilder.loadTexts:userTrap9.setStatus('')
userTrap10=NotificationType((1,3,6,1,4,1,34278,0,15))
if mibBuilder.loadTexts:userTrap10.setStatus('')
userTrap11=NotificationType((1,3,6,1,4,1,34278,0,16))
if mibBuilder.loadTexts:userTrap11.setStatus('')
userTrap12=NotificationType((1,3,6,1,4,1,34278,0,17))
if mibBuilder.loadTexts:userTrap12.setStatus('')
userTrap13=NotificationType((1,3,6,1,4,1,34278,0,18))
if mibBuilder.loadTexts:userTrap13.setStatus('')
userTrap14=NotificationType((1,3,6,1,4,1,34278,0,19))
if mibBuilder.loadTexts:userTrap14.setStatus('')
userTrap15=NotificationType((1,3,6,1,4,1,34278,0,20))
if mibBuilder.loadTexts:userTrap15.setStatus('')
userTrap16=NotificationType((1,3,6,1,4,1,34278,0,21))
if mibBuilder.loadTexts:userTrap16.setStatus('')
mibBuilder.exportSymbols('JANITZA-MIB',**{'system':system,'sysDescr':sysDescr,'sysObjectID':sysObjectID,_E:sysUpTime,'sysName':sysName,'sysLocation':sysLocation,'sysServices':sysServices,'snmp':snmp,'coldStart':coldStart,'warmStart':warmStart,'janitza':janitza,'userTrap1':userTrap1,'userTrap2':userTrap2,'userTrap3':userTrap3,'userTrap4':userTrap4,'userTrap5':userTrap5,'userTrap6':userTrap6,'userTrap7':userTrap7,'userTrap8':userTrap8,'userTrap9':userTrap9,'userTrap10':userTrap10,'userTrap11':userTrap11,'userTrap12':userTrap12,'userTrap13':userTrap13,'userTrap14':userTrap14,'userTrap15':userTrap15,'userTrap16':userTrap16,'rmsPhase':rmsPhase,'uLN1':uLN1,'uLN2':uLN2,'uLN3':uLN3,'uLN4':uLN4,'uL1L2':uL1L2,'uL2L3':uL2L3,'uL3L1':uL3L1,'iL1':iL1,'iL2':iL2,'iL3':iL3,'iL4':iL4,'pL1':pL1,'pL2':pL2,'pL3':pL3,'pL4':pL4,'qL1':qL1,'qL2':qL2,'qL3':qL3,'qL4':qL4,'sL1':sL1,'sL2':sL2,'sL3':sL3,'sL4':sL4,'cosPL1':cosPL1,'cosPL2':cosPL2,'cosPL3':cosPL3,'cosPL4':cosPL4,'rmsSumme3':rmsSumme3,'p3':p3,'q3':q3,'s3':s3,'cosP3':cosP3,'rmsSumme4':rmsSumme4,'p4':p4,'q4':q4,'s4':s4,'cosP4':cosP4,'energiePhase':energiePhase,'whL1':whL1,'whL2':whL2,'whL3':whL3,'whL4':whL4,'qhL1':qhL1,'qhL2':qhL2,'qhL3':qhL3,'qhL4':qhL4,'energieSumme3':energieSumme3,'wh3':wh3,'qh3':qh3,'energieSumme4':energieSumme4,'wh4':wh4,'qh4':qh4,'thd':thd,'thdULN1':thdULN1,'thdULN2':thdULN2,'thdULN3':thdULN3,'thdULN4':thdULN4,'thdIL1':thdIL1,'thdIL2':thdIL2,'thdIL3':thdIL3,'thdIL4':thdIL4,'misc':misc,'frequenz':frequenz,'user':user,'jasicVAR1':jasicVAR1,'jasicVAR2':jasicVAR2,'jasicVAR3':jasicVAR3,'jasicVAR4':jasicVAR4,'jasicVAR5':jasicVAR5,'jasicVAR6':jasicVAR6,'jasicVAR7':jasicVAR7,'jasicVAR8':jasicVAR8,'jasicVAR9':jasicVAR9,'jasicVAR10':jasicVAR10,'jasicVAR11':jasicVAR11,'jasicVAR12':jasicVAR12,'jasicVAR13':jasicVAR13,'jasicVAR14':jasicVAR14,'jasicVAR15':jasicVAR15,'jasicVAR16':jasicVAR16})