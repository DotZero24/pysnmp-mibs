_U='hpnsaSWRevisionHistoryEntry'
_T='hpnsaSWBIOSFirmwareIndex'
_S='hpnsaSWDriversIndex'
_R='Driver'
_Q='Service'
_P='Paused'
_O='Pause_Pending'
_N='Continue_Pending'
_M='Running'
_L='Stop_Pending'
_K='Start_Pending'
_J='Stopped'
_I='hpnsaSWManageabilityIndex'
_H='read-write'
_G='Unknown'
_F='HPNSASOFTWARESUBSYSTEM-MIB'
_E='OctetString'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaSW_ObjectIdentity=ObjectIdentity
hpnsaSW=_HpnsaSW_ObjectIdentity((1,3,6,1,4,1,11,2,23,24))
_HpnsaSWMibRev_ObjectIdentity=ObjectIdentity
hpnsaSWMibRev=_HpnsaSWMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,24,1))
class _HpnsaSWMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaSWMibRevMajor_Type.__name__=_D
_HpnsaSWMibRevMajor_Object=MibScalar
hpnsaSWMibRevMajor=_HpnsaSWMibRevMajor_Object((1,3,6,1,4,1,11,2,23,24,1,1),_HpnsaSWMibRevMajor_Type())
hpnsaSWMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWMibRevMajor.setStatus(_A)
class _HpnsaSWMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaSWMibRevMinor_Type.__name__=_D
_HpnsaSWMibRevMinor_Object=MibScalar
hpnsaSWMibRevMinor=_HpnsaSWMibRevMinor_Object((1,3,6,1,4,1,11,2,23,24,1,2),_HpnsaSWMibRevMinor_Type())
hpnsaSWMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWMibRevMinor.setStatus(_A)
_HpnsaSWManageability_ObjectIdentity=ObjectIdentity
hpnsaSWManageability=_HpnsaSWManageability_ObjectIdentity((1,3,6,1,4,1,11,2,23,24,2))
_HpnsaSWManageabilityTable_Object=MibTable
hpnsaSWManageabilityTable=_HpnsaSWManageabilityTable_Object((1,3,6,1,4,1,11,2,23,24,2,1))
if mibBuilder.loadTexts:hpnsaSWManageabilityTable.setStatus(_A)
_HpnsaSWManageabilityEntry_Object=MibTableRow
hpnsaSWManageabilityEntry=_HpnsaSWManageabilityEntry_Object((1,3,6,1,4,1,11,2,23,24,2,1,1))
hpnsaSWManageabilityEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:hpnsaSWManageabilityEntry.setStatus(_A)
_HpnsaSWManageabilityIndex_Type=Integer32
_HpnsaSWManageabilityIndex_Object=MibTableColumn
hpnsaSWManageabilityIndex=_HpnsaSWManageabilityIndex_Object((1,3,6,1,4,1,11,2,23,24,2,1,1,1),_HpnsaSWManageabilityIndex_Type())
hpnsaSWManageabilityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWManageabilityIndex.setStatus(_A)
class _HpnsaSWManageabilityFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnsaSWManageabilityFileName_Type.__name__=_C
_HpnsaSWManageabilityFileName_Object=MibTableColumn
hpnsaSWManageabilityFileName=_HpnsaSWManageabilityFileName_Object((1,3,6,1,4,1,11,2,23,24,2,1,1,2),_HpnsaSWManageabilityFileName_Type())
hpnsaSWManageabilityFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWManageabilityFileName.setStatus(_A)
class _HpnsaSWManageabilityFileSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnsaSWManageabilityFileSize_Type.__name__=_C
_HpnsaSWManageabilityFileSize_Object=MibTableColumn
hpnsaSWManageabilityFileSize=_HpnsaSWManageabilityFileSize_Object((1,3,6,1,4,1,11,2,23,24,2,1,1,3),_HpnsaSWManageabilityFileSize_Type())
hpnsaSWManageabilityFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWManageabilityFileSize.setStatus(_A)
class _HpnsaSWManageabilityFileDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaSWManageabilityFileDate_Type.__name__=_E
_HpnsaSWManageabilityFileDate_Object=MibTableColumn
hpnsaSWManageabilityFileDate=_HpnsaSWManageabilityFileDate_Object((1,3,6,1,4,1,11,2,23,24,2,1,1,4),_HpnsaSWManageabilityFileDate_Type())
hpnsaSWManageabilityFileDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWManageabilityFileDate.setStatus(_A)
class _HpnsaSWManageabilityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_HpnsaSWManageabilityState_Type.__name__=_D
_HpnsaSWManageabilityState_Object=MibTableColumn
hpnsaSWManageabilityState=_HpnsaSWManageabilityState_Object((1,3,6,1,4,1,11,2,23,24,2,1,1,5),_HpnsaSWManageabilityState_Type())
hpnsaSWManageabilityState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWManageabilityState.setStatus(_A)
class _HpnsaSWManageabilityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),('Agent',1),(_Q,2),(_R,3),('Other',4)))
_HpnsaSWManageabilityType_Type.__name__=_D
_HpnsaSWManageabilityType_Object=MibTableColumn
hpnsaSWManageabilityType=_HpnsaSWManageabilityType_Object((1,3,6,1,4,1,11,2,23,24,2,1,1,6),_HpnsaSWManageabilityType_Type())
hpnsaSWManageabilityType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWManageabilityType.setStatus(_A)
class _HpnsaSWManageabilityVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HpnsaSWManageabilityVersion_Type.__name__=_C
_HpnsaSWManageabilityVersion_Object=MibTableColumn
hpnsaSWManageabilityVersion=_HpnsaSWManageabilityVersion_Object((1,3,6,1,4,1,11,2,23,24,2,1,1,7),_HpnsaSWManageabilityVersion_Type())
hpnsaSWManageabilityVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWManageabilityVersion.setStatus(_A)
class _HpnsaSWManageabilityDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnsaSWManageabilityDescription_Type.__name__=_C
_HpnsaSWManageabilityDescription_Object=MibTableColumn
hpnsaSWManageabilityDescription=_HpnsaSWManageabilityDescription_Object((1,3,6,1,4,1,11,2,23,24,2,1,1,8),_HpnsaSWManageabilityDescription_Type())
hpnsaSWManageabilityDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWManageabilityDescription.setStatus(_A)
_HpnsaSWDrivers_ObjectIdentity=ObjectIdentity
hpnsaSWDrivers=_HpnsaSWDrivers_ObjectIdentity((1,3,6,1,4,1,11,2,23,24,3))
_HpnsaSWDriversTable_Object=MibTable
hpnsaSWDriversTable=_HpnsaSWDriversTable_Object((1,3,6,1,4,1,11,2,23,24,3,1))
if mibBuilder.loadTexts:hpnsaSWDriversTable.setStatus(_A)
_HpnsaSWDriversEntry_Object=MibTableRow
hpnsaSWDriversEntry=_HpnsaSWDriversEntry_Object((1,3,6,1,4,1,11,2,23,24,3,1,1))
hpnsaSWDriversEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:hpnsaSWDriversEntry.setStatus(_A)
class _HpnsaSWDriversIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaSWDriversIndex_Type.__name__=_D
_HpnsaSWDriversIndex_Object=MibTableColumn
hpnsaSWDriversIndex=_HpnsaSWDriversIndex_Object((1,3,6,1,4,1,11,2,23,24,3,1,1,1),_HpnsaSWDriversIndex_Type())
hpnsaSWDriversIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWDriversIndex.setStatus(_A)
class _HpnsaSWDriversFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnsaSWDriversFileName_Type.__name__=_C
_HpnsaSWDriversFileName_Object=MibTableColumn
hpnsaSWDriversFileName=_HpnsaSWDriversFileName_Object((1,3,6,1,4,1,11,2,23,24,3,1,1,2),_HpnsaSWDriversFileName_Type())
hpnsaSWDriversFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWDriversFileName.setStatus(_A)
class _HpnsaSWDriversFileSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnsaSWDriversFileSize_Type.__name__=_C
_HpnsaSWDriversFileSize_Object=MibTableColumn
hpnsaSWDriversFileSize=_HpnsaSWDriversFileSize_Object((1,3,6,1,4,1,11,2,23,24,3,1,1,3),_HpnsaSWDriversFileSize_Type())
hpnsaSWDriversFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWDriversFileSize.setStatus(_A)
class _HpnsaSWDriversFileDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaSWDriversFileDate_Type.__name__=_E
_HpnsaSWDriversFileDate_Object=MibTableColumn
hpnsaSWDriversFileDate=_HpnsaSWDriversFileDate_Object((1,3,6,1,4,1,11,2,23,24,3,1,1,4),_HpnsaSWDriversFileDate_Type())
hpnsaSWDriversFileDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWDriversFileDate.setStatus(_A)
class _HpnsaSWDriversState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7)))
_HpnsaSWDriversState_Type.__name__=_D
_HpnsaSWDriversState_Object=MibTableColumn
hpnsaSWDriversState=_HpnsaSWDriversState_Object((1,3,6,1,4,1,11,2,23,24,3,1,1,5),_HpnsaSWDriversState_Type())
hpnsaSWDriversState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWDriversState.setStatus(_A)
class _HpnsaSWDriversType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),('NetworkInterfaceCard',1),('SCSI',2),('DiskArrayController',3),('System',4)))
_HpnsaSWDriversType_Type.__name__=_D
_HpnsaSWDriversType_Object=MibTableColumn
hpnsaSWDriversType=_HpnsaSWDriversType_Object((1,3,6,1,4,1,11,2,23,24,3,1,1,6),_HpnsaSWDriversType_Type())
hpnsaSWDriversType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWDriversType.setStatus(_A)
class _HpnsaSWDriversVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HpnsaSWDriversVersion_Type.__name__=_C
_HpnsaSWDriversVersion_Object=MibTableColumn
hpnsaSWDriversVersion=_HpnsaSWDriversVersion_Object((1,3,6,1,4,1,11,2,23,24,3,1,1,7),_HpnsaSWDriversVersion_Type())
hpnsaSWDriversVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWDriversVersion.setStatus(_A)
class _HpnsaSWDriversDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnsaSWDriversDescription_Type.__name__=_C
_HpnsaSWDriversDescription_Object=MibTableColumn
hpnsaSWDriversDescription=_HpnsaSWDriversDescription_Object((1,3,6,1,4,1,11,2,23,24,3,1,1,8),_HpnsaSWDriversDescription_Type())
hpnsaSWDriversDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWDriversDescription.setStatus(_A)
_HpnsaSWBIOSFirmware_ObjectIdentity=ObjectIdentity
hpnsaSWBIOSFirmware=_HpnsaSWBIOSFirmware_ObjectIdentity((1,3,6,1,4,1,11,2,23,24,4))
_HpnsaSWBIOSFirmwareTable_Object=MibTable
hpnsaSWBIOSFirmwareTable=_HpnsaSWBIOSFirmwareTable_Object((1,3,6,1,4,1,11,2,23,24,4,1))
if mibBuilder.loadTexts:hpnsaSWBIOSFirmwareTable.setStatus(_A)
_HpnsaSWBIOSFirmwareEntry_Object=MibTableRow
hpnsaSWBIOSFirmwareEntry=_HpnsaSWBIOSFirmwareEntry_Object((1,3,6,1,4,1,11,2,23,24,4,1,1))
hpnsaSWBIOSFirmwareEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:hpnsaSWBIOSFirmwareEntry.setStatus(_A)
class _HpnsaSWBIOSFirmwareIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaSWBIOSFirmwareIndex_Type.__name__=_D
_HpnsaSWBIOSFirmwareIndex_Object=MibTableColumn
hpnsaSWBIOSFirmwareIndex=_HpnsaSWBIOSFirmwareIndex_Object((1,3,6,1,4,1,11,2,23,24,4,1,1,1),_HpnsaSWBIOSFirmwareIndex_Type())
hpnsaSWBIOSFirmwareIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWBIOSFirmwareIndex.setStatus(_A)
class _HpnsaSWBIOSFirmwareName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnsaSWBIOSFirmwareName_Type.__name__=_C
_HpnsaSWBIOSFirmwareName_Object=MibTableColumn
hpnsaSWBIOSFirmwareName=_HpnsaSWBIOSFirmwareName_Object((1,3,6,1,4,1,11,2,23,24,4,1,1,2),_HpnsaSWBIOSFirmwareName_Type())
hpnsaSWBIOSFirmwareName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWBIOSFirmwareName.setStatus(_A)
_HpnsaSWBIOSFirmwareType_Type=Integer32
_HpnsaSWBIOSFirmwareType_Object=MibTableColumn
hpnsaSWBIOSFirmwareType=_HpnsaSWBIOSFirmwareType_Object((1,3,6,1,4,1,11,2,23,24,4,1,1,3),_HpnsaSWBIOSFirmwareType_Type())
hpnsaSWBIOSFirmwareType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWBIOSFirmwareType.setStatus(_A)
class _HpnsaSWBIOSFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HpnsaSWBIOSFirmwareVersion_Type.__name__=_C
_HpnsaSWBIOSFirmwareVersion_Object=MibTableColumn
hpnsaSWBIOSFirmwareVersion=_HpnsaSWBIOSFirmwareVersion_Object((1,3,6,1,4,1,11,2,23,24,4,1,1,4),_HpnsaSWBIOSFirmwareVersion_Type())
hpnsaSWBIOSFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWBIOSFirmwareVersion.setStatus(_A)
class _HpnsaSWBIOSFirmwareDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnsaSWBIOSFirmwareDescription_Type.__name__=_C
_HpnsaSWBIOSFirmwareDescription_Object=MibTableColumn
hpnsaSWBIOSFirmwareDescription=_HpnsaSWBIOSFirmwareDescription_Object((1,3,6,1,4,1,11,2,23,24,4,1,1,5),_HpnsaSWBIOSFirmwareDescription_Type())
hpnsaSWBIOSFirmwareDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWBIOSFirmwareDescription.setStatus(_A)
_HpnsaSWRevisionHistory_ObjectIdentity=ObjectIdentity
hpnsaSWRevisionHistory=_HpnsaSWRevisionHistory_ObjectIdentity((1,3,6,1,4,1,11,2,23,24,5))
_HpnsaSWRevisionHistoryTable_Object=MibTable
hpnsaSWRevisionHistoryTable=_HpnsaSWRevisionHistoryTable_Object((1,3,6,1,4,1,11,2,23,24,5,1))
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryTable.setStatus(_A)
_HpnsaSWRevisionHistoryEntry_Object=MibTableRow
hpnsaSWRevisionHistoryEntry=_HpnsaSWRevisionHistoryEntry_Object((1,3,6,1,4,1,11,2,23,24,5,1,1))
hpnsaSWRevisionHistoryEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryEntry.setStatus(_A)
_HpnsaSWRevisionHistoryIndex_Type=Integer32
_HpnsaSWRevisionHistoryIndex_Object=MibTableColumn
hpnsaSWRevisionHistoryIndex=_HpnsaSWRevisionHistoryIndex_Object((1,3,6,1,4,1,11,2,23,24,5,1,1,1),_HpnsaSWRevisionHistoryIndex_Type())
hpnsaSWRevisionHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryIndex.setStatus(_A)
class _HpnsaSWRevisionHistoryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnsaSWRevisionHistoryName_Type.__name__=_C
_HpnsaSWRevisionHistoryName_Object=MibTableColumn
hpnsaSWRevisionHistoryName=_HpnsaSWRevisionHistoryName_Object((1,3,6,1,4,1,11,2,23,24,5,1,1,2),_HpnsaSWRevisionHistoryName_Type())
hpnsaSWRevisionHistoryName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryName.setStatus(_A)
class _HpnsaSWRevisionHistorySize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnsaSWRevisionHistorySize_Type.__name__=_C
_HpnsaSWRevisionHistorySize_Object=MibTableColumn
hpnsaSWRevisionHistorySize=_HpnsaSWRevisionHistorySize_Object((1,3,6,1,4,1,11,2,23,24,5,1,1,3),_HpnsaSWRevisionHistorySize_Type())
hpnsaSWRevisionHistorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWRevisionHistorySize.setStatus(_A)
class _HpnsaSWRevisionHistoryDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaSWRevisionHistoryDate_Type.__name__=_E
_HpnsaSWRevisionHistoryDate_Object=MibTableColumn
hpnsaSWRevisionHistoryDate=_HpnsaSWRevisionHistoryDate_Object((1,3,6,1,4,1,11,2,23,24,5,1,1,4),_HpnsaSWRevisionHistoryDate_Type())
hpnsaSWRevisionHistoryDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryDate.setStatus(_A)
class _HpnsaSWRevisionHistoryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaSWRevisionHistoryState_Type.__name__=_D
_HpnsaSWRevisionHistoryState_Object=MibTableColumn
hpnsaSWRevisionHistoryState=_HpnsaSWRevisionHistoryState_Object((1,3,6,1,4,1,11,2,23,24,5,1,1,5),_HpnsaSWRevisionHistoryState_Type())
hpnsaSWRevisionHistoryState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryState.setStatus(_A)
class _HpnsaSWRevisionHistoryCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),('Agent',1),(_Q,2),(_R,3),('BIOSFirmware',4)))
_HpnsaSWRevisionHistoryCategory_Type.__name__=_D
_HpnsaSWRevisionHistoryCategory_Object=MibTableColumn
hpnsaSWRevisionHistoryCategory=_HpnsaSWRevisionHistoryCategory_Object((1,3,6,1,4,1,11,2,23,24,5,1,1,6),_HpnsaSWRevisionHistoryCategory_Type())
hpnsaSWRevisionHistoryCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryCategory.setStatus(_A)
class _HpnsaSWRevisionHistoryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaSWRevisionHistoryType_Type.__name__=_D
_HpnsaSWRevisionHistoryType_Object=MibTableColumn
hpnsaSWRevisionHistoryType=_HpnsaSWRevisionHistoryType_Object((1,3,6,1,4,1,11,2,23,24,5,1,1,7),_HpnsaSWRevisionHistoryType_Type())
hpnsaSWRevisionHistoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryType.setStatus(_A)
class _HpnsaSWRevisionHistoryVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HpnsaSWRevisionHistoryVersion_Type.__name__=_C
_HpnsaSWRevisionHistoryVersion_Object=MibTableColumn
hpnsaSWRevisionHistoryVersion=_HpnsaSWRevisionHistoryVersion_Object((1,3,6,1,4,1,11,2,23,24,5,1,1,8),_HpnsaSWRevisionHistoryVersion_Type())
hpnsaSWRevisionHistoryVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryVersion.setStatus(_A)
class _HpnsaSWRevisionHistoryChangeDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaSWRevisionHistoryChangeDate_Type.__name__=_E
_HpnsaSWRevisionHistoryChangeDate_Object=MibTableColumn
hpnsaSWRevisionHistoryChangeDate=_HpnsaSWRevisionHistoryChangeDate_Object((1,3,6,1,4,1,11,2,23,24,5,1,1,9),_HpnsaSWRevisionHistoryChangeDate_Type())
hpnsaSWRevisionHistoryChangeDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryChangeDate.setStatus(_A)
class _HpnsaSWAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HpnsaSWAgentVersion_Type.__name__=_C
_HpnsaSWAgentVersion_Object=MibScalar
hpnsaSWAgentVersion=_HpnsaSWAgentVersion_Object((1,3,6,1,4,1,11,2,23,24,6),_HpnsaSWAgentVersion_Type())
hpnsaSWAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaSWAgentVersion.setStatus(_A)
class _HpnsaSWPollingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HpnsaSWPollingState_Type.__name__=_D
_HpnsaSWPollingState_Object=MibScalar
hpnsaSWPollingState=_HpnsaSWPollingState_Object((1,3,6,1,4,1,11,2,23,24,7),_HpnsaSWPollingState_Type())
hpnsaSWPollingState.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnsaSWPollingState.setStatus(_A)
_HpnsaSWPollingTime_Type=Integer32
_HpnsaSWPollingTime_Object=MibScalar
hpnsaSWPollingTime=_HpnsaSWPollingTime_Object((1,3,6,1,4,1,11,2,23,24,8),_HpnsaSWPollingTime_Type())
hpnsaSWPollingTime.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnsaSWPollingTime.setStatus(_A)
class _HpnsaSWManualPolling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1234));namedValues=NamedValues(('CheckRevisionHistory',1234))
_HpnsaSWManualPolling_Type.__name__=_D
_HpnsaSWManualPolling_Object=MibScalar
hpnsaSWManualPolling=_HpnsaSWManualPolling_Object((1,3,6,1,4,1,11,2,23,24,9),_HpnsaSWManualPolling_Type())
hpnsaSWManualPolling.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnsaSWManualPolling.setStatus(_A)
class _HpnsaSWRevisionHistoryReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1234));namedValues=NamedValues(('ClearHistory',1234))
_HpnsaSWRevisionHistoryReset_Type.__name__=_D
_HpnsaSWRevisionHistoryReset_Object=MibScalar
hpnsaSWRevisionHistoryReset=_HpnsaSWRevisionHistoryReset_Object((1,3,6,1,4,1,11,2,23,24,10),_HpnsaSWRevisionHistoryReset_Type())
hpnsaSWRevisionHistoryReset.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnsaSWRevisionHistoryReset.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaSW':hpnsaSW,'hpnsaSWMibRev':hpnsaSWMibRev,'hpnsaSWMibRevMajor':hpnsaSWMibRevMajor,'hpnsaSWMibRevMinor':hpnsaSWMibRevMinor,'hpnsaSWManageability':hpnsaSWManageability,'hpnsaSWManageabilityTable':hpnsaSWManageabilityTable,'hpnsaSWManageabilityEntry':hpnsaSWManageabilityEntry,_I:hpnsaSWManageabilityIndex,'hpnsaSWManageabilityFileName':hpnsaSWManageabilityFileName,'hpnsaSWManageabilityFileSize':hpnsaSWManageabilityFileSize,'hpnsaSWManageabilityFileDate':hpnsaSWManageabilityFileDate,'hpnsaSWManageabilityState':hpnsaSWManageabilityState,'hpnsaSWManageabilityType':hpnsaSWManageabilityType,'hpnsaSWManageabilityVersion':hpnsaSWManageabilityVersion,'hpnsaSWManageabilityDescription':hpnsaSWManageabilityDescription,'hpnsaSWDrivers':hpnsaSWDrivers,'hpnsaSWDriversTable':hpnsaSWDriversTable,'hpnsaSWDriversEntry':hpnsaSWDriversEntry,_S:hpnsaSWDriversIndex,'hpnsaSWDriversFileName':hpnsaSWDriversFileName,'hpnsaSWDriversFileSize':hpnsaSWDriversFileSize,'hpnsaSWDriversFileDate':hpnsaSWDriversFileDate,'hpnsaSWDriversState':hpnsaSWDriversState,'hpnsaSWDriversType':hpnsaSWDriversType,'hpnsaSWDriversVersion':hpnsaSWDriversVersion,'hpnsaSWDriversDescription':hpnsaSWDriversDescription,'hpnsaSWBIOSFirmware':hpnsaSWBIOSFirmware,'hpnsaSWBIOSFirmwareTable':hpnsaSWBIOSFirmwareTable,'hpnsaSWBIOSFirmwareEntry':hpnsaSWBIOSFirmwareEntry,_T:hpnsaSWBIOSFirmwareIndex,'hpnsaSWBIOSFirmwareName':hpnsaSWBIOSFirmwareName,'hpnsaSWBIOSFirmwareType':hpnsaSWBIOSFirmwareType,'hpnsaSWBIOSFirmwareVersion':hpnsaSWBIOSFirmwareVersion,'hpnsaSWBIOSFirmwareDescription':hpnsaSWBIOSFirmwareDescription,'hpnsaSWRevisionHistory':hpnsaSWRevisionHistory,'hpnsaSWRevisionHistoryTable':hpnsaSWRevisionHistoryTable,_U:hpnsaSWRevisionHistoryEntry,'hpnsaSWRevisionHistoryIndex':hpnsaSWRevisionHistoryIndex,'hpnsaSWRevisionHistoryName':hpnsaSWRevisionHistoryName,'hpnsaSWRevisionHistorySize':hpnsaSWRevisionHistorySize,'hpnsaSWRevisionHistoryDate':hpnsaSWRevisionHistoryDate,'hpnsaSWRevisionHistoryState':hpnsaSWRevisionHistoryState,'hpnsaSWRevisionHistoryCategory':hpnsaSWRevisionHistoryCategory,'hpnsaSWRevisionHistoryType':hpnsaSWRevisionHistoryType,'hpnsaSWRevisionHistoryVersion':hpnsaSWRevisionHistoryVersion,'hpnsaSWRevisionHistoryChangeDate':hpnsaSWRevisionHistoryChangeDate,'hpnsaSWAgentVersion':hpnsaSWAgentVersion,'hpnsaSWPollingState':hpnsaSWPollingState,'hpnsaSWPollingTime':hpnsaSWPollingTime,'hpnsaSWManualPolling':hpnsaSWManualPolling,'hpnsaSWRevisionHistoryReset':hpnsaSWRevisionHistoryReset})