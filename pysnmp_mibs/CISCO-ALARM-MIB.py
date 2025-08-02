_N='coiAlarmDescription'
_M='coiAlarmStatus'
_L='coiAlarmSeverity'
_K='coiAlarmObjectName'
_J='2019-08-28 00:00'
_I='coiAlarmType'
_H='coiAlarmObjectEntPhyIndex'
_G='coiAlarmObjectIfIndex'
_F='coiAlarmIndex'
_E='unknown'
_D='Integer32'
_C='read-only'
_B='CISCO-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoAlarmMIB=ModuleIdentity((1,3,6,1,4,1,9,9,869))
if mibBuilder.loadTexts:ciscoAlarmMIB.setRevisions(('2021-05-17 00:00',_J,_J))
class CoiAlarmObjectTypeClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68)));namedValues=NamedValues(*((_E,1),('hwMemorySbe',2),('hwMemoryMbe',3),('hwMemoryParity',4),('hwFreeze',5),('hwFlopError',6),('hwInternal',7),('hwTimeout',8),('hwHang',9),('hwError',10),('hwLinkCrc',11),('hwCodeViolation',12),('hwLinkDisparity',13),('hwEnvmonSensorAlarm',14),('hwEnvmonPemAlarm',15),('hwEnvmonFanAlarm',16),('swMemoryFault',17),('swBusError',18),('swProcessCrash',19),('swMallocError',20),('swFoobar',21),('swConnectFail',22),('swProcessRestart',23),('swProcessFailure',24),('swMandatoryProcessFailure',25),('swServiceRestart',26),('swServiceFailure',27),('swPmHeartbeat',28),('swHostosHeartbeat',29),('swCccWdog',30),('hwConfigErr',31),('hwGenericErr',32),('hwIndirectErr',33),('hwOorThreshErr',34),('hwUnexpectedErr',35),('hwBoardReload',36),('hwSliceReload',37),('hwMiscErr',38),('hwRxResourceErr',39),('hwTxResourceErr',40),('hwLinkStatChange',41),('hwEtherBridge',42),('swInitErr',43),('swMiscErr',44),('hwEnvmonEcuAlarm',45),('hwEnvmonPwrFilterAlarm',46),('hwSonet',47),('hwG709',48),('hwEthernet',49),('hwOptics',50),('hwGfp',51),('hwSdhController',52),('swFsdbaggPlane',53),('hwOts',54),('swMacsecMka',55),('swSmartLicErr',56),('swProvisionErr',57),('hwSyncec',58),('hwPci',59),('swWdDiskUsage',60),('swCfgmgr',61),('swG709Otnsec',62),('hwCpri',63),('hwImfpga',64),('swFsdbaggConnMismatch',65),('hwFibreChannel',66),('hwE1',67),('hwCem',68)))
_CiscoAlarmMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoAlarmMIBNotifs=_CiscoAlarmMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,869,0))
_CiscoAlarmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAlarmMIBObjects=_CiscoAlarmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,869,1))
_CoiAlarmActive_ObjectIdentity=ObjectIdentity
coiAlarmActive=_CoiAlarmActive_ObjectIdentity((1,3,6,1,4,1,9,9,869,1,1))
_CoiAlarmActiveTable_Object=MibTable
coiAlarmActiveTable=_CoiAlarmActiveTable_Object((1,3,6,1,4,1,9,9,869,1,1,1))
if mibBuilder.loadTexts:coiAlarmActiveTable.setStatus(_A)
_CoiAlarmActiveEntry_Object=MibTableRow
coiAlarmActiveEntry=_CoiAlarmActiveEntry_Object((1,3,6,1,4,1,9,9,869,1,1,1,1))
coiAlarmActiveEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:coiAlarmActiveEntry.setStatus(_A)
_CoiAlarmIndex_Type=Integer32
_CoiAlarmIndex_Object=MibTableColumn
coiAlarmIndex=_CoiAlarmIndex_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,1),_CoiAlarmIndex_Type())
coiAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmIndex.setStatus(_A)
_CoiAlarmObjectIfIndex_Type=InterfaceIndexOrZero
_CoiAlarmObjectIfIndex_Object=MibTableColumn
coiAlarmObjectIfIndex=_CoiAlarmObjectIfIndex_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,2),_CoiAlarmObjectIfIndex_Type())
coiAlarmObjectIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmObjectIfIndex.setStatus(_A)
_CoiAlarmObjectEntPhyIndex_Type=EntPhysicalIndexOrZero
_CoiAlarmObjectEntPhyIndex_Object=MibTableColumn
coiAlarmObjectEntPhyIndex=_CoiAlarmObjectEntPhyIndex_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,3),_CoiAlarmObjectEntPhyIndex_Type())
coiAlarmObjectEntPhyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmObjectEntPhyIndex.setStatus(_A)
_CoiAlarmObjectName_Type=DisplayString
_CoiAlarmObjectName_Object=MibTableColumn
coiAlarmObjectName=_CoiAlarmObjectName_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,4),_CoiAlarmObjectName_Type())
coiAlarmObjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmObjectName.setStatus(_A)
_CoiAlarmObjectType_Type=CoiAlarmObjectTypeClass
_CoiAlarmObjectType_Object=MibTableColumn
coiAlarmObjectType=_CoiAlarmObjectType_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,5),_CoiAlarmObjectType_Type())
coiAlarmObjectType.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmObjectType.setStatus(_A)
_CoiAlarmType_Type=DisplayString
_CoiAlarmType_Object=MibTableColumn
coiAlarmType=_CoiAlarmType_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,6),_CoiAlarmType_Type())
coiAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmType.setStatus(_A)
_CoiAlarmTimeStamp_Type=Counter64
_CoiAlarmTimeStamp_Object=MibTableColumn
coiAlarmTimeStamp=_CoiAlarmTimeStamp_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,7),_CoiAlarmTimeStamp_Type())
coiAlarmTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmTimeStamp.setStatus(_A)
class _CoiAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_E,0),('notReported',1),('notAlarmed',2),('minor',3),('major',4),('critical',5)))
_CoiAlarmSeverity_Type.__name__=_D
_CoiAlarmSeverity_Object=MibTableColumn
coiAlarmSeverity=_CoiAlarmSeverity_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,8),_CoiAlarmSeverity_Type())
coiAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmSeverity.setStatus(_A)
class _CoiAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('set',1),('clear',2),('suppress',3)))
_CoiAlarmStatus_Type.__name__=_D
_CoiAlarmStatus_Object=MibTableColumn
coiAlarmStatus=_CoiAlarmStatus_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,9),_CoiAlarmStatus_Type())
coiAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmStatus.setStatus(_A)
class _CoiAlarmServiceAffecting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('notServiceAffecting',1),('serviceAffecting',2)))
_CoiAlarmServiceAffecting_Type.__name__=_D
_CoiAlarmServiceAffecting_Object=MibTableColumn
coiAlarmServiceAffecting=_CoiAlarmServiceAffecting_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,10),_CoiAlarmServiceAffecting_Type())
coiAlarmServiceAffecting.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmServiceAffecting.setStatus(_A)
_CoiAlarmDescription_Type=DisplayString
_CoiAlarmDescription_Object=MibTableColumn
coiAlarmDescription=_CoiAlarmDescription_Object((1,3,6,1,4,1,9,9,869,1,1,1,1,11),_CoiAlarmDescription_Type())
coiAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:coiAlarmDescription.setStatus(_A)
coiAlarmStatusChange=NotificationType((1,3,6,1,4,1,9,9,869,0,1))
coiAlarmStatusChange.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_K),(_B,_I),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:coiAlarmStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CoiAlarmObjectTypeClass':CoiAlarmObjectTypeClass,'ciscoAlarmMIB':ciscoAlarmMIB,'ciscoAlarmMIBNotifs':ciscoAlarmMIBNotifs,'coiAlarmStatusChange':coiAlarmStatusChange,'ciscoAlarmMIBObjects':ciscoAlarmMIBObjects,'coiAlarmActive':coiAlarmActive,'coiAlarmActiveTable':coiAlarmActiveTable,'coiAlarmActiveEntry':coiAlarmActiveEntry,_F:coiAlarmIndex,_G:coiAlarmObjectIfIndex,_H:coiAlarmObjectEntPhyIndex,_K:coiAlarmObjectName,'coiAlarmObjectType':coiAlarmObjectType,_I:coiAlarmType,'coiAlarmTimeStamp':coiAlarmTimeStamp,_L:coiAlarmSeverity,_M:coiAlarmStatus,'coiAlarmServiceAffecting':coiAlarmServiceAffecting,_N:coiAlarmDescription})