_O='ledOFF'
_N='hpnsaSiFloppyDriveIndex'
_M='hpnsaSiPortIndex'
_L='hpnsaSiCPUIndex'
_K='hpnsaSiAgentIndex'
_J='OctetString'
_I='HPNSASINFO-MIB'
_H='enabled'
_G='disabled'
_F='n-a'
_E='optional'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaSystemInfo_ObjectIdentity=ObjectIdentity
hpnsaSystemInfo=_HpnsaSystemInfo_ObjectIdentity((1,3,6,1,4,1,11,2,23,7))
_HpnsaSiMibRev_ObjectIdentity=ObjectIdentity
hpnsaSiMibRev=_HpnsaSiMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,7,1))
class _HpnsaSiMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaSiMibRevMajor_Type.__name__=_C
_HpnsaSiMibRevMajor_Object=MibScalar
hpnsaSiMibRevMajor=_HpnsaSiMibRevMajor_Object((1,3,6,1,4,1,11,2,23,7,1,1),_HpnsaSiMibRevMajor_Type())
hpnsaSiMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiMibRevMajor.setStatus(_A)
class _HpnsaSiMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaSiMibRevMinor_Type.__name__=_C
_HpnsaSiMibRevMinor_Object=MibScalar
hpnsaSiMibRevMinor=_HpnsaSiMibRevMinor_Object((1,3,6,1,4,1,11,2,23,7,1,2),_HpnsaSiMibRevMinor_Type())
hpnsaSiMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiMibRevMinor.setStatus(_A)
_HpnsaSiAgent_ObjectIdentity=ObjectIdentity
hpnsaSiAgent=_HpnsaSiAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,7,2))
_HpnsaSiAgentTable_Object=MibTable
hpnsaSiAgentTable=_HpnsaSiAgentTable_Object((1,3,6,1,4,1,11,2,23,7,2,1))
if mibBuilder.loadTexts:hpnsaSiAgentTable.setStatus(_A)
_HpnsaSiAgentEntry_Object=MibTableRow
hpnsaSiAgentEntry=_HpnsaSiAgentEntry_Object((1,3,6,1,4,1,11,2,23,7,2,1,1))
hpnsaSiAgentEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:hpnsaSiAgentEntry.setStatus(_A)
class _HpnsaSiAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaSiAgentIndex_Type.__name__=_C
_HpnsaSiAgentIndex_Object=MibTableColumn
hpnsaSiAgentIndex=_HpnsaSiAgentIndex_Object((1,3,6,1,4,1,11,2,23,7,2,1,1,1),_HpnsaSiAgentIndex_Type())
hpnsaSiAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiAgentIndex.setStatus(_A)
class _HpnsaSiAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiAgentName_Type.__name__=_D
_HpnsaSiAgentName_Object=MibTableColumn
hpnsaSiAgentName=_HpnsaSiAgentName_Object((1,3,6,1,4,1,11,2,23,7,2,1,1,2),_HpnsaSiAgentName_Type())
hpnsaSiAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiAgentName.setStatus(_A)
class _HpnsaSiAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnsaSiAgentVersion_Type.__name__=_D
_HpnsaSiAgentVersion_Object=MibTableColumn
hpnsaSiAgentVersion=_HpnsaSiAgentVersion_Object((1,3,6,1,4,1,11,2,23,7,2,1,1,3),_HpnsaSiAgentVersion_Type())
hpnsaSiAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiAgentVersion.setStatus(_A)
class _HpnsaSiAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_HpnsaSiAgentDate_Type.__name__=_J
_HpnsaSiAgentDate_Object=MibTableColumn
hpnsaSiAgentDate=_HpnsaSiAgentDate_Object((1,3,6,1,4,1,11,2,23,7,2,1,1,4),_HpnsaSiAgentDate_Type())
hpnsaSiAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiAgentDate.setStatus(_A)
_HpnsaSiBasicInfo_ObjectIdentity=ObjectIdentity
hpnsaSiBasicInfo=_HpnsaSiBasicInfo_ObjectIdentity((1,3,6,1,4,1,11,2,23,7,3))
class _HpnsaSiModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,35,36,40,42,52,54,61,63,65,66,67,68,69,71,72,73,75,79,80,82,83,84,85,86,87,88,89)));namedValues=NamedValues(*(('HP_Vectra_PC',0),('HP_Vectra_ES_12_PC',1),('HP_Vectra_RS_20_PC',2),('HP_Vectra_PortableCS_PC',3),('HP_Vectra_ES_PC',4),('HP_Vectra_CS_PC',5),('HP_Vectra_RS_16_PC',6),('HP_Vectra_QS_16_PC',7),('HP_Vectra_QS_20_PC',8),('HP_Vectra_RS_20C_PC',9),('HP_Vectra_RS_25C_PC',10),('HP_Vectra_LS_286_PC',11),('HP_Vectra_QS_16S_PC',12),('HP_Vectra_386_25_PC',13),('HP_Vectra_486_25T_PC',14),('HP_Vectra_286_12_PC',15),('HP_Vectra_486_33T_PC',16),('HP_Vectra_386_20_PC',17),('HP_Vectra_386_16N_PC',18),('HP_Vectra_386_20N_PC',19),('HP_Vectra_486s_20_PC',20),('HP_Vectra_386s_20_PC',21),('HP_Vectra_486_25U_PC',22),('HP_Vectra_486_33U_PC',23),('HP_Vectra_486_50U_PC',24),('HP_Vectra_486_66U_PC',25),('HP_Vectra_486_ST_Series',26),('HP_Vectra_386_25N',27),('HP_Vectra_486_N',28),('HP_Vectra_386s_25',29),('HP_Vectra_386_33N',30),('HP_Vectra_486_33N',32),('HP_NetServer_LE_Series',35),('HP_NetServer_LM_Series',36),('HP_NetServer_LF_Series',40),('HP_NetServer_LS_Series',42),('HP_NetServer_LD_Series',52),('HP_NetServer_Racks_Series',54),('HP_NetServer_LC_Series',61),('HP_NetServer_LH_Series',63),('HP_NetServer_LX_Series',65),('HP_NetServer_LH3000',66),('HP_NetServer_LH6000',67),('HP_NetServer_LC2000',68),('HP_NetServer_LT6000',69),('HP_NetServer_E_Series',71),('HP_NetServer_LP1000r',72),('HP_NetServer_LP2000r',73),('HP_NetServer_tc6100',75),('HP_NetServer_tc3100',79),('HP_NetServer_tc4100',80),('HP_NetServer_lh6000u3',82),('HP_NetServer_lt6000ru3',83),('HP_NetServer_lc2000u3',84),('HP_NetServer_lh3000u3',85),('HP_NetServer_lp1000r',86),('HP_NetServer_lp2000r',87),('HP_NetServer_tc7100',88),('HP_NetServer_rc7100',89)))
_HpnsaSiModel_Type.__name__=_C
_HpnsaSiModel_Object=MibScalar
hpnsaSiModel=_HpnsaSiModel_Object((1,3,6,1,4,1,11,2,23,7,3,1),_HpnsaSiModel_Type())
hpnsaSiModel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiModel.setStatus(_A)
class _HpnsaSiBIOSVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiBIOSVersion_Type.__name__=_D
_HpnsaSiBIOSVersion_Object=MibScalar
hpnsaSiBIOSVersion=_HpnsaSiBIOSVersion_Object((1,3,6,1,4,1,11,2,23,7,3,2),_HpnsaSiBIOSVersion_Type())
hpnsaSiBIOSVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiBIOSVersion.setStatus(_A)
class _HpnsaSiVideoBIOSVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiVideoBIOSVersion_Type.__name__=_D
_HpnsaSiVideoBIOSVersion_Object=MibScalar
hpnsaSiVideoBIOSVersion=_HpnsaSiVideoBIOSVersion_Object((1,3,6,1,4,1,11,2,23,7,3,3),_HpnsaSiVideoBIOSVersion_Type())
hpnsaSiVideoBIOSVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiVideoBIOSVersion.setStatus(_E)
class _HpnsaSiSCSIBIOSVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiSCSIBIOSVersion_Type.__name__=_D
_HpnsaSiSCSIBIOSVersion_Object=MibScalar
hpnsaSiSCSIBIOSVersion=_HpnsaSiSCSIBIOSVersion_Object((1,3,6,1,4,1,11,2,23,7,3,4),_HpnsaSiSCSIBIOSVersion_Type())
hpnsaSiSCSIBIOSVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiSCSIBIOSVersion.setStatus(_A)
_HpnsaSiNumEISASlots_Type=Integer32
_HpnsaSiNumEISASlots_Object=MibScalar
hpnsaSiNumEISASlots=_HpnsaSiNumEISASlots_Object((1,3,6,1,4,1,11,2,23,7,3,5),_HpnsaSiNumEISASlots_Type())
hpnsaSiNumEISASlots.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiNumEISASlots.setStatus(_A)
_HpnsaSiNumPCISlots_Type=Integer32
_HpnsaSiNumPCISlots_Object=MibScalar
hpnsaSiNumPCISlots=_HpnsaSiNumPCISlots_Object((1,3,6,1,4,1,11,2,23,7,3,6),_HpnsaSiNumPCISlots_Type())
hpnsaSiNumPCISlots.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiNumPCISlots.setStatus(_A)
_HpnsaSiNumCPU_Type=Integer32
_HpnsaSiNumCPU_Object=MibScalar
hpnsaSiNumCPU=_HpnsaSiNumCPU_Object((1,3,6,1,4,1,11,2,23,7,3,7),_HpnsaSiNumCPU_Type())
hpnsaSiNumCPU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiNumCPU.setStatus(_A)
_HpnsaSiCPUTable_Object=MibTable
hpnsaSiCPUTable=_HpnsaSiCPUTable_Object((1,3,6,1,4,1,11,2,23,7,3,8))
if mibBuilder.loadTexts:hpnsaSiCPUTable.setStatus(_A)
_HpnsaSiCPUEntry_Object=MibTableRow
hpnsaSiCPUEntry=_HpnsaSiCPUEntry_Object((1,3,6,1,4,1,11,2,23,7,3,8,1))
hpnsaSiCPUEntry.setIndexNames((0,_I,_L))
if mibBuilder.loadTexts:hpnsaSiCPUEntry.setStatus(_A)
class _HpnsaSiCPUIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaSiCPUIndex_Type.__name__=_C
_HpnsaSiCPUIndex_Object=MibTableColumn
hpnsaSiCPUIndex=_HpnsaSiCPUIndex_Object((1,3,6,1,4,1,11,2,23,7,3,8,1,1),_HpnsaSiCPUIndex_Type())
hpnsaSiCPUIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiCPUIndex.setStatus(_A)
class _HpnsaSiCPUModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,253,254,255)));namedValues=NamedValues(*(('CPU_80286',0),('CPU_8088',1),('CPU_8086',2),('CPU_80386',3),('CPU_80386_SX',4),('CPU_486_DX',5),('CPU_486_SX',6),('CPU_486_DX2_or_OverDrive',8),('CPU_486_P23T',9),('CPU_487_SX',10),('CPU_Pentium',11),('CPU_Pentium_OverDrive',12),('CPU_486_24C',13),('CPU_Pentium_Series_P54C',14),('CPU_Pentium_Series_P54CT',15),('CPU_Pentium_Series_P54CM',16),('CPU_486_SX2',17),('CPU_486_SL',18),('CPU_Pentium_Series_P6',19),('CPU_Pentium_II',20),('CPU_Pentium_II_Xeon',21),('CPU_Pentium_III',22),('CPU_Pentium_III_Xeon',23),('notPresent',253),('CPU_Dual_Pentium',254),('CPU_Unknown',255)))
_HpnsaSiCPUModel_Type.__name__=_C
_HpnsaSiCPUModel_Object=MibTableColumn
hpnsaSiCPUModel=_HpnsaSiCPUModel_Object((1,3,6,1,4,1,11,2,23,7,3,8,1,2),_HpnsaSiCPUModel_Type())
hpnsaSiCPUModel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiCPUModel.setStatus(_A)
_HpnsaSiCPUSpeed_Type=Integer32
_HpnsaSiCPUSpeed_Object=MibTableColumn
hpnsaSiCPUSpeed=_HpnsaSiCPUSpeed_Object((1,3,6,1,4,1,11,2,23,7,3,8,1,3),_HpnsaSiCPUSpeed_Type())
hpnsaSiCPUSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiCPUSpeed.setStatus(_A)
class _HpnsaSiOpSysType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiOpSysType_Type.__name__=_D
_HpnsaSiOpSysType_Object=MibScalar
hpnsaSiOpSysType=_HpnsaSiOpSysType_Object((1,3,6,1,4,1,11,2,23,7,3,9),_HpnsaSiOpSysType_Type())
hpnsaSiOpSysType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiOpSysType.setStatus(_A)
class _HpnsaSiOpSysVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiOpSysVer_Type.__name__=_D
_HpnsaSiOpSysVer_Object=MibScalar
hpnsaSiOpSysVer=_HpnsaSiOpSysVer_Object((1,3,6,1,4,1,11,2,23,7,3,10),_HpnsaSiOpSysVer_Type())
hpnsaSiOpSysVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiOpSysVer.setStatus(_A)
class _HpnsaSiSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiSystemName_Type.__name__=_D
_HpnsaSiSystemName_Object=MibScalar
hpnsaSiSystemName=_HpnsaSiSystemName_Object((1,3,6,1,4,1,11,2,23,7,3,11),_HpnsaSiSystemName_Type())
hpnsaSiSystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiSystemName.setStatus(_A)
class _HpnsaSiSystemID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiSystemID_Type.__name__=_D
_HpnsaSiSystemID_Object=MibScalar
hpnsaSiSystemID=_HpnsaSiSystemID_Object((1,3,6,1,4,1,11,2,23,7,3,12),_HpnsaSiSystemID_Type())
hpnsaSiSystemID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiSystemID.setStatus(_E)
class _HpnsaSiKbdType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiKbdType_Type.__name__=_D
_HpnsaSiKbdType_Object=MibScalar
hpnsaSiKbdType=_HpnsaSiKbdType_Object((1,3,6,1,4,1,11,2,23,7,3,13),_HpnsaSiKbdType_Type())
hpnsaSiKbdType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiKbdType.setStatus(_E)
class _HpnsaSiMouseType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiMouseType_Type.__name__=_D
_HpnsaSiMouseType_Object=MibScalar
hpnsaSiMouseType=_HpnsaSiMouseType_Object((1,3,6,1,4,1,11,2,23,7,3,14),_HpnsaSiMouseType_Type())
hpnsaSiMouseType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiMouseType.setStatus(_E)
class _HpnsaSiVideoType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiVideoType_Type.__name__=_D
_HpnsaSiVideoType_Object=MibScalar
hpnsaSiVideoType=_HpnsaSiVideoType_Object((1,3,6,1,4,1,11,2,23,7,3,15),_HpnsaSiVideoType_Type())
hpnsaSiVideoType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiVideoType.setStatus(_E)
_HpnsaSiNumISASlots_Type=Integer32
_HpnsaSiNumISASlots_Object=MibScalar
hpnsaSiNumISASlots=_HpnsaSiNumISASlots_Object((1,3,6,1,4,1,11,2,23,7,3,16),_HpnsaSiNumISASlots_Type())
hpnsaSiNumISASlots.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiNumISASlots.setStatus(_A)
class _HpnsaSiModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiModelName_Type.__name__=_D
_HpnsaSiModelName_Object=MibScalar
hpnsaSiModelName=_HpnsaSiModelName_Object((1,3,6,1,4,1,11,2,23,7,3,17),_HpnsaSiModelName_Type())
hpnsaSiModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiModelName.setStatus(_A)
class _HpnsaSiOpSysDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaSiOpSysDescription_Type.__name__=_D
_HpnsaSiOpSysDescription_Object=MibScalar
hpnsaSiOpSysDescription=_HpnsaSiOpSysDescription_Object((1,3,6,1,4,1,11,2,23,7,3,18),_HpnsaSiOpSysDescription_Type())
hpnsaSiOpSysDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiOpSysDescription.setStatus(_A)
_HpnsaSiSecurity_ObjectIdentity=ObjectIdentity
hpnsaSiSecurity=_HpnsaSiSecurity_ObjectIdentity((1,3,6,1,4,1,11,2,23,7,4))
class _HpnsaSiPowerOnPassword_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2)))
_HpnsaSiPowerOnPassword_Type.__name__=_C
_HpnsaSiPowerOnPassword_Object=MibScalar
hpnsaSiPowerOnPassword=_HpnsaSiPowerOnPassword_Object((1,3,6,1,4,1,11,2,23,7,4,1),_HpnsaSiPowerOnPassword_Type())
hpnsaSiPowerOnPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiPowerOnPassword.setStatus(_A)
class _HpnsaSiNetServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2)))
_HpnsaSiNetServerMode_Type.__name__=_C
_HpnsaSiNetServerMode_Object=MibScalar
hpnsaSiNetServerMode=_HpnsaSiNetServerMode_Object((1,3,6,1,4,1,11,2,23,7,4,2),_HpnsaSiNetServerMode_Type())
hpnsaSiNetServerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiNetServerMode.setStatus(_A)
class _HpnsaSiKeyboardLockPassword_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2)))
_HpnsaSiKeyboardLockPassword_Type.__name__=_C
_HpnsaSiKeyboardLockPassword_Object=MibScalar
hpnsaSiKeyboardLockPassword=_HpnsaSiKeyboardLockPassword_Object((1,3,6,1,4,1,11,2,23,7,4,3),_HpnsaSiKeyboardLockPassword_Type())
hpnsaSiKeyboardLockPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiKeyboardLockPassword.setStatus(_A)
class _HpnsaSiVideoBlankMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2)))
_HpnsaSiVideoBlankMode_Type.__name__=_C
_HpnsaSiVideoBlankMode_Object=MibScalar
hpnsaSiVideoBlankMode=_HpnsaSiVideoBlankMode_Object((1,3,6,1,4,1,11,2,23,7,4,4),_HpnsaSiVideoBlankMode_Type())
hpnsaSiVideoBlankMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiVideoBlankMode.setStatus(_A)
class _HpnsaSiBootDiskPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),('c-then-a',1),('a-then-c',2),('c-only',3),('a-only',4)))
_HpnsaSiBootDiskPriority_Type.__name__=_C
_HpnsaSiBootDiskPriority_Object=MibScalar
hpnsaSiBootDiskPriority=_HpnsaSiBootDiskPriority_Object((1,3,6,1,4,1,11,2,23,7,4,5),_HpnsaSiBootDiskPriority_Type())
hpnsaSiBootDiskPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiBootDiskPriority.setStatus(_A)
class _HpnsaSiWriteToFloppy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2)))
_HpnsaSiWriteToFloppy_Type.__name__=_C
_HpnsaSiWriteToFloppy_Object=MibScalar
hpnsaSiWriteToFloppy=_HpnsaSiWriteToFloppy_Object((1,3,6,1,4,1,11,2,23,7,4,6),_HpnsaSiWriteToFloppy_Type())
hpnsaSiWriteToFloppy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiWriteToFloppy.setStatus(_A)
class _HpnsaSiKbdMouseInactivityTO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2)))
_HpnsaSiKbdMouseInactivityTO_Type.__name__=_C
_HpnsaSiKbdMouseInactivityTO_Object=MibScalar
hpnsaSiKbdMouseInactivityTO=_HpnsaSiKbdMouseInactivityTO_Object((1,3,6,1,4,1,11,2,23,7,4,7),_HpnsaSiKbdMouseInactivityTO_Type())
hpnsaSiKbdMouseInactivityTO.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiKbdMouseInactivityTO.setStatus(_A)
_HpnsaSiPort_ObjectIdentity=ObjectIdentity
hpnsaSiPort=_HpnsaSiPort_ObjectIdentity((1,3,6,1,4,1,11,2,23,7,5))
_HpnsaSiPortTable_Object=MibTable
hpnsaSiPortTable=_HpnsaSiPortTable_Object((1,3,6,1,4,1,11,2,23,7,5,1))
if mibBuilder.loadTexts:hpnsaSiPortTable.setStatus(_A)
_HpnsaSiPortEntry_Object=MibTableRow
hpnsaSiPortEntry=_HpnsaSiPortEntry_Object((1,3,6,1,4,1,11,2,23,7,5,1,1))
hpnsaSiPortEntry.setIndexNames((0,_I,_M))
if mibBuilder.loadTexts:hpnsaSiPortEntry.setStatus(_A)
_HpnsaSiPortIndex_Type=Integer32
_HpnsaSiPortIndex_Object=MibTableColumn
hpnsaSiPortIndex=_HpnsaSiPortIndex_Object((1,3,6,1,4,1,11,2,23,7,5,1,1,1),_HpnsaSiPortIndex_Type())
hpnsaSiPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiPortIndex.setStatus(_A)
class _HpnsaSiPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('serial',1),('parallel',2)))
_HpnsaSiPortType_Type.__name__=_C
_HpnsaSiPortType_Object=MibTableColumn
hpnsaSiPortType=_HpnsaSiPortType_Object((1,3,6,1,4,1,11,2,23,7,5,1,1,2),_HpnsaSiPortType_Type())
hpnsaSiPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiPortType.setStatus(_A)
_HpnsaSiPortStartAddress_Type=Integer32
_HpnsaSiPortStartAddress_Object=MibTableColumn
hpnsaSiPortStartAddress=_HpnsaSiPortStartAddress_Object((1,3,6,1,4,1,11,2,23,7,5,1,1,3),_HpnsaSiPortStartAddress_Type())
hpnsaSiPortStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiPortStartAddress.setStatus(_A)
_HpnsaSiPortEndAddress_Type=Integer32
_HpnsaSiPortEndAddress_Object=MibTableColumn
hpnsaSiPortEndAddress=_HpnsaSiPortEndAddress_Object((1,3,6,1,4,1,11,2,23,7,5,1,1,4),_HpnsaSiPortEndAddress_Type())
hpnsaSiPortEndAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiPortEndAddress.setStatus(_A)
_HpnsaSiPortInterruptNum_Type=Integer32
_HpnsaSiPortInterruptNum_Object=MibTableColumn
hpnsaSiPortInterruptNum=_HpnsaSiPortInterruptNum_Object((1,3,6,1,4,1,11,2,23,7,5,1,1,5),_HpnsaSiPortInterruptNum_Type())
hpnsaSiPortInterruptNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiPortInterruptNum.setStatus(_A)
_HpnsaSiMemory_ObjectIdentity=ObjectIdentity
hpnsaSiMemory=_HpnsaSiMemory_ObjectIdentity((1,3,6,1,4,1,11,2,23,7,6))
class _HpnsaSiBaseMemSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnsaSiBaseMemSize_Type.__name__=_C
_HpnsaSiBaseMemSize_Object=MibScalar
hpnsaSiBaseMemSize=_HpnsaSiBaseMemSize_Object((1,3,6,1,4,1,11,2,23,7,6,1),_HpnsaSiBaseMemSize_Type())
hpnsaSiBaseMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiBaseMemSize.setStatus(_A)
class _HpnsaSiExtMemSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnsaSiExtMemSize_Type.__name__=_C
_HpnsaSiExtMemSize_Object=MibScalar
hpnsaSiExtMemSize=_HpnsaSiExtMemSize_Object((1,3,6,1,4,1,11,2,23,7,6,2),_HpnsaSiExtMemSize_Type())
hpnsaSiExtMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiExtMemSize.setStatus(_A)
class _HpnsaSiMemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('other',0),('on-board',1),('singleWidthModule',2),('doubleWidthModule',3),('simm',4)))
_HpnsaSiMemType_Type.__name__=_C
_HpnsaSiMemType_Object=MibScalar
hpnsaSiMemType=_HpnsaSiMemType_Object((1,3,6,1,4,1,11,2,23,7,6,3),_HpnsaSiMemType_Type())
hpnsaSiMemType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiMemType.setStatus(_E)
class _HpnsaSiMemSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaSiMemSpeed_Type.__name__=_C
_HpnsaSiMemSpeed_Object=MibScalar
hpnsaSiMemSpeed=_HpnsaSiMemSpeed_Object((1,3,6,1,4,1,11,2,23,7,6,4),_HpnsaSiMemSpeed_Type())
hpnsaSiMemSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiMemSpeed.setStatus(_E)
_HpnsaSiFloppyDrive_ObjectIdentity=ObjectIdentity
hpnsaSiFloppyDrive=_HpnsaSiFloppyDrive_ObjectIdentity((1,3,6,1,4,1,11,2,23,7,8))
_HpnsaSiNumFloppyDrives_Type=Integer32
_HpnsaSiNumFloppyDrives_Object=MibScalar
hpnsaSiNumFloppyDrives=_HpnsaSiNumFloppyDrives_Object((1,3,6,1,4,1,11,2,23,7,8,1),_HpnsaSiNumFloppyDrives_Type())
hpnsaSiNumFloppyDrives.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiNumFloppyDrives.setStatus(_A)
_HpnsaSiFloppyDriveTable_Object=MibTable
hpnsaSiFloppyDriveTable=_HpnsaSiFloppyDriveTable_Object((1,3,6,1,4,1,11,2,23,7,8,2))
if mibBuilder.loadTexts:hpnsaSiFloppyDriveTable.setStatus(_A)
_HpnsaSiFloppyDriveEntry_Object=MibTableRow
hpnsaSiFloppyDriveEntry=_HpnsaSiFloppyDriveEntry_Object((1,3,6,1,4,1,11,2,23,7,8,2,1))
hpnsaSiFloppyDriveEntry.setIndexNames((0,_I,_N))
if mibBuilder.loadTexts:hpnsaSiFloppyDriveEntry.setStatus(_A)
_HpnsaSiFloppyDriveIndex_Type=Integer32
_HpnsaSiFloppyDriveIndex_Object=MibTableColumn
hpnsaSiFloppyDriveIndex=_HpnsaSiFloppyDriveIndex_Object((1,3,6,1,4,1,11,2,23,7,8,2,1,1),_HpnsaSiFloppyDriveIndex_Type())
hpnsaSiFloppyDriveIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiFloppyDriveIndex.setStatus(_A)
class _HpnsaSiFloppyDriveType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unknown',0),('m-360K',1),('m-1-2MB',2),('m-1-2-MB',3),('m-1-44MB',4)))
_HpnsaSiFloppyDriveType_Type.__name__=_C
_HpnsaSiFloppyDriveType_Object=MibTableColumn
hpnsaSiFloppyDriveType=_HpnsaSiFloppyDriveType_Object((1,3,6,1,4,1,11,2,23,7,8,2,1,2),_HpnsaSiFloppyDriveType_Type())
hpnsaSiFloppyDriveType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiFloppyDriveType.setStatus(_A)
_HpnsaSiRemoteLocatorLED_ObjectIdentity=ObjectIdentity
hpnsaSiRemoteLocatorLED=_HpnsaSiRemoteLocatorLED_ObjectIdentity((1,3,6,1,4,1,11,2,23,7,9))
class _HpnsaSiRemoteLocatorLEDSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notSupported',0),('Supported',1)))
_HpnsaSiRemoteLocatorLEDSupported_Type.__name__=_C
_HpnsaSiRemoteLocatorLEDSupported_Object=MibScalar
hpnsaSiRemoteLocatorLEDSupported=_HpnsaSiRemoteLocatorLEDSupported_Object((1,3,6,1,4,1,11,2,23,7,9,1),_HpnsaSiRemoteLocatorLEDSupported_Type())
hpnsaSiRemoteLocatorLEDSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiRemoteLocatorLEDSupported.setStatus(_A)
class _HpnsaSiRemoteLocatorLEDStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),('ledON',1)))
_HpnsaSiRemoteLocatorLEDStatus_Type.__name__=_C
_HpnsaSiRemoteLocatorLEDStatus_Object=MibScalar
hpnsaSiRemoteLocatorLEDStatus=_HpnsaSiRemoteLocatorLEDStatus_Object((1,3,6,1,4,1,11,2,23,7,9,2),_HpnsaSiRemoteLocatorLEDStatus_Type())
hpnsaSiRemoteLocatorLEDStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSiRemoteLocatorLEDStatus.setStatus(_A)
class _HpnsaSiRemoteLocatorLEDSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),('ledON',1)))
_HpnsaSiRemoteLocatorLEDSet_Type.__name__=_C
_HpnsaSiRemoteLocatorLEDSet_Object=MibScalar
hpnsaSiRemoteLocatorLEDSet=_HpnsaSiRemoteLocatorLEDSet_Object((1,3,6,1,4,1,11,2,23,7,9,3),_HpnsaSiRemoteLocatorLEDSet_Type())
hpnsaSiRemoteLocatorLEDSet.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnsaSiRemoteLocatorLEDSet.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaSystemInfo':hpnsaSystemInfo,'hpnsaSiMibRev':hpnsaSiMibRev,'hpnsaSiMibRevMajor':hpnsaSiMibRevMajor,'hpnsaSiMibRevMinor':hpnsaSiMibRevMinor,'hpnsaSiAgent':hpnsaSiAgent,'hpnsaSiAgentTable':hpnsaSiAgentTable,'hpnsaSiAgentEntry':hpnsaSiAgentEntry,_K:hpnsaSiAgentIndex,'hpnsaSiAgentName':hpnsaSiAgentName,'hpnsaSiAgentVersion':hpnsaSiAgentVersion,'hpnsaSiAgentDate':hpnsaSiAgentDate,'hpnsaSiBasicInfo':hpnsaSiBasicInfo,'hpnsaSiModel':hpnsaSiModel,'hpnsaSiBIOSVersion':hpnsaSiBIOSVersion,'hpnsaSiVideoBIOSVersion':hpnsaSiVideoBIOSVersion,'hpnsaSiSCSIBIOSVersion':hpnsaSiSCSIBIOSVersion,'hpnsaSiNumEISASlots':hpnsaSiNumEISASlots,'hpnsaSiNumPCISlots':hpnsaSiNumPCISlots,'hpnsaSiNumCPU':hpnsaSiNumCPU,'hpnsaSiCPUTable':hpnsaSiCPUTable,'hpnsaSiCPUEntry':hpnsaSiCPUEntry,_L:hpnsaSiCPUIndex,'hpnsaSiCPUModel':hpnsaSiCPUModel,'hpnsaSiCPUSpeed':hpnsaSiCPUSpeed,'hpnsaSiOpSysType':hpnsaSiOpSysType,'hpnsaSiOpSysVer':hpnsaSiOpSysVer,'hpnsaSiSystemName':hpnsaSiSystemName,'hpnsaSiSystemID':hpnsaSiSystemID,'hpnsaSiKbdType':hpnsaSiKbdType,'hpnsaSiMouseType':hpnsaSiMouseType,'hpnsaSiVideoType':hpnsaSiVideoType,'hpnsaSiNumISASlots':hpnsaSiNumISASlots,'hpnsaSiModelName':hpnsaSiModelName,'hpnsaSiOpSysDescription':hpnsaSiOpSysDescription,'hpnsaSiSecurity':hpnsaSiSecurity,'hpnsaSiPowerOnPassword':hpnsaSiPowerOnPassword,'hpnsaSiNetServerMode':hpnsaSiNetServerMode,'hpnsaSiKeyboardLockPassword':hpnsaSiKeyboardLockPassword,'hpnsaSiVideoBlankMode':hpnsaSiVideoBlankMode,'hpnsaSiBootDiskPriority':hpnsaSiBootDiskPriority,'hpnsaSiWriteToFloppy':hpnsaSiWriteToFloppy,'hpnsaSiKbdMouseInactivityTO':hpnsaSiKbdMouseInactivityTO,'hpnsaSiPort':hpnsaSiPort,'hpnsaSiPortTable':hpnsaSiPortTable,'hpnsaSiPortEntry':hpnsaSiPortEntry,_M:hpnsaSiPortIndex,'hpnsaSiPortType':hpnsaSiPortType,'hpnsaSiPortStartAddress':hpnsaSiPortStartAddress,'hpnsaSiPortEndAddress':hpnsaSiPortEndAddress,'hpnsaSiPortInterruptNum':hpnsaSiPortInterruptNum,'hpnsaSiMemory':hpnsaSiMemory,'hpnsaSiBaseMemSize':hpnsaSiBaseMemSize,'hpnsaSiExtMemSize':hpnsaSiExtMemSize,'hpnsaSiMemType':hpnsaSiMemType,'hpnsaSiMemSpeed':hpnsaSiMemSpeed,'hpnsaSiFloppyDrive':hpnsaSiFloppyDrive,'hpnsaSiNumFloppyDrives':hpnsaSiNumFloppyDrives,'hpnsaSiFloppyDriveTable':hpnsaSiFloppyDriveTable,'hpnsaSiFloppyDriveEntry':hpnsaSiFloppyDriveEntry,_N:hpnsaSiFloppyDriveIndex,'hpnsaSiFloppyDriveType':hpnsaSiFloppyDriveType,'hpnsaSiRemoteLocatorLED':hpnsaSiRemoteLocatorLED,'hpnsaSiRemoteLocatorLEDSupported':hpnsaSiRemoteLocatorLEDSupported,'hpnsaSiRemoteLocatorLEDStatus':hpnsaSiRemoteLocatorLEDStatus,'hpnsaSiRemoteLocatorLEDSet':hpnsaSiRemoteLocatorLEDSet})