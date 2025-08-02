_S='percentage'
_R='absolute'
_Q='Integer32'
_P='OctetString'
_O='read-write'
_N='h3cResMonAdditionalInfo'
_M='h3cResMonTotal'
_L='h3cResMonFree'
_K='h3cResMonCurrent'
_J='h3cResMonSevereThreshold'
_I='h3cResMonMinorThreshold'
_H='h3cResMonThresholdUnit'
_G='read-only'
_F='h3cResMonResourceName'
_E='h3cResMonCpuIndex'
_D='h3cResMonSlotIndex'
_C='h3cResMonChassisIndex'
_B='current'
_A='H3C-RES-MON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Q,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cResMon=ModuleIdentity((1,3,6,1,4,1,2011,10,2,169))
if mibBuilder.loadTexts:h3cResMon.setRevisions(('2017-04-01 00:00',))
_H3cResMonScalarObjects_ObjectIdentity=ObjectIdentity
h3cResMonScalarObjects=_H3cResMonScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,169,1))
_H3cResMonMinorResendEnable_Type=TruthValue
_H3cResMonMinorResendEnable_Object=MibScalar
h3cResMonMinorResendEnable=_H3cResMonMinorResendEnable_Object((1,3,6,1,4,1,2011,10,2,169,1,1),_H3cResMonMinorResendEnable_Type())
h3cResMonMinorResendEnable.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cResMonMinorResendEnable.setStatus(_B)
class _H3cResMonOutputEnable_Type(Bits):namedValues=NamedValues(*(('syslog',0),('snmpNotification',1),('netconfEvent',2)))
_H3cResMonOutputEnable_Type.__name__='Bits'
_H3cResMonOutputEnable_Object=MibScalar
h3cResMonOutputEnable=_H3cResMonOutputEnable_Object((1,3,6,1,4,1,2011,10,2,169,1,2),_H3cResMonOutputEnable_Type())
h3cResMonOutputEnable.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cResMonOutputEnable.setStatus(_B)
_H3cResMonTables_ObjectIdentity=ObjectIdentity
h3cResMonTables=_H3cResMonTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,169,2))
_H3cResMonConfigTable_Object=MibTable
h3cResMonConfigTable=_H3cResMonConfigTable_Object((1,3,6,1,4,1,2011,10,2,169,2,1))
if mibBuilder.loadTexts:h3cResMonConfigTable.setStatus(_B)
_H3cResMonConfigEntry_Object=MibTableRow
h3cResMonConfigEntry=_H3cResMonConfigEntry_Object((1,3,6,1,4,1,2011,10,2,169,2,1,1))
h3cResMonConfigEntry.setIndexNames((0,_A,_C),(0,_A,_D),(0,_A,_E),(0,_A,_F))
if mibBuilder.loadTexts:h3cResMonConfigEntry.setStatus(_B)
_H3cResMonChassisIndex_Type=Unsigned32
_H3cResMonChassisIndex_Object=MibTableColumn
h3cResMonChassisIndex=_H3cResMonChassisIndex_Object((1,3,6,1,4,1,2011,10,2,169,2,1,1,1),_H3cResMonChassisIndex_Type())
h3cResMonChassisIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cResMonChassisIndex.setStatus(_B)
_H3cResMonSlotIndex_Type=Unsigned32
_H3cResMonSlotIndex_Object=MibTableColumn
h3cResMonSlotIndex=_H3cResMonSlotIndex_Object((1,3,6,1,4,1,2011,10,2,169,2,1,1,2),_H3cResMonSlotIndex_Type())
h3cResMonSlotIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cResMonSlotIndex.setStatus(_B)
_H3cResMonCpuIndex_Type=Unsigned32
_H3cResMonCpuIndex_Object=MibTableColumn
h3cResMonCpuIndex=_H3cResMonCpuIndex_Object((1,3,6,1,4,1,2011,10,2,169,2,1,1,3),_H3cResMonCpuIndex_Type())
h3cResMonCpuIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cResMonCpuIndex.setStatus(_B)
class _H3cResMonResourceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cResMonResourceName_Type.__name__=_P
_H3cResMonResourceName_Object=MibTableColumn
h3cResMonResourceName=_H3cResMonResourceName_Object((1,3,6,1,4,1,2011,10,2,169,2,1,1,4),_H3cResMonResourceName_Type())
h3cResMonResourceName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cResMonResourceName.setStatus(_B)
class _H3cResMonThresholdUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_H3cResMonThresholdUnit_Type.__name__=_Q
_H3cResMonThresholdUnit_Object=MibTableColumn
h3cResMonThresholdUnit=_H3cResMonThresholdUnit_Object((1,3,6,1,4,1,2011,10,2,169,2,1,1,5),_H3cResMonThresholdUnit_Type())
h3cResMonThresholdUnit.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cResMonThresholdUnit.setStatus(_B)
_H3cResMonMinorThreshold_Type=Unsigned32
_H3cResMonMinorThreshold_Object=MibTableColumn
h3cResMonMinorThreshold=_H3cResMonMinorThreshold_Object((1,3,6,1,4,1,2011,10,2,169,2,1,1,6),_H3cResMonMinorThreshold_Type())
h3cResMonMinorThreshold.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cResMonMinorThreshold.setStatus(_B)
_H3cResMonSevereThreshold_Type=Unsigned32
_H3cResMonSevereThreshold_Object=MibTableColumn
h3cResMonSevereThreshold=_H3cResMonSevereThreshold_Object((1,3,6,1,4,1,2011,10,2,169,2,1,1,7),_H3cResMonSevereThreshold_Type())
h3cResMonSevereThreshold.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cResMonSevereThreshold.setStatus(_B)
_H3cResMonInfoTable_Object=MibTable
h3cResMonInfoTable=_H3cResMonInfoTable_Object((1,3,6,1,4,1,2011,10,2,169,2,2))
if mibBuilder.loadTexts:h3cResMonInfoTable.setStatus(_B)
_H3cResMonInfoEntry_Object=MibTableRow
h3cResMonInfoEntry=_H3cResMonInfoEntry_Object((1,3,6,1,4,1,2011,10,2,169,2,2,1))
h3cResMonInfoEntry.setIndexNames((0,_A,_C),(0,_A,_D),(0,_A,_E),(0,_A,_F))
if mibBuilder.loadTexts:h3cResMonInfoEntry.setStatus(_B)
class _H3cResMonUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_H3cResMonUnit_Type.__name__=_Q
_H3cResMonUnit_Object=MibTableColumn
h3cResMonUnit=_H3cResMonUnit_Object((1,3,6,1,4,1,2011,10,2,169,2,2,1,1),_H3cResMonUnit_Type())
h3cResMonUnit.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cResMonUnit.setStatus(_B)
_H3cResMonCurrent_Type=Unsigned32
_H3cResMonCurrent_Object=MibTableColumn
h3cResMonCurrent=_H3cResMonCurrent_Object((1,3,6,1,4,1,2011,10,2,169,2,2,1,2),_H3cResMonCurrent_Type())
h3cResMonCurrent.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cResMonCurrent.setStatus(_B)
_H3cResMonFree_Type=Unsigned32
_H3cResMonFree_Object=MibTableColumn
h3cResMonFree=_H3cResMonFree_Object((1,3,6,1,4,1,2011,10,2,169,2,2,1,3),_H3cResMonFree_Type())
h3cResMonFree.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cResMonFree.setStatus(_B)
_H3cResMonTotal_Type=Unsigned32
_H3cResMonTotal_Object=MibTableColumn
h3cResMonTotal=_H3cResMonTotal_Object((1,3,6,1,4,1,2011,10,2,169,2,2,1,4),_H3cResMonTotal_Type())
h3cResMonTotal.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cResMonTotal.setStatus(_B)
_H3cResMonNotification_ObjectIdentity=ObjectIdentity
h3cResMonNotification=_H3cResMonNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,169,3))
_H3cResMonTrapPrefix_ObjectIdentity=ObjectIdentity
h3cResMonTrapPrefix=_H3cResMonTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,169,3,0))
_H3cResMonTrapInfor_ObjectIdentity=ObjectIdentity
h3cResMonTrapInfor=_H3cResMonTrapInfor_ObjectIdentity((1,3,6,1,4,1,2011,10,2,169,3,1))
class _H3cResMonAdditionalInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cResMonAdditionalInfo_Type.__name__=_P
_H3cResMonAdditionalInfo_Object=MibScalar
h3cResMonAdditionalInfo=_H3cResMonAdditionalInfo_Object((1,3,6,1,4,1,2011,10,2,169,3,1,1),_H3cResMonAdditionalInfo_Type())
h3cResMonAdditionalInfo.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cResMonAdditionalInfo.setStatus(_B)
h3cResMonMinorNotification=NotificationType((1,3,6,1,4,1,2011,10,2,169,3,0,1))
h3cResMonMinorNotification.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:h3cResMonMinorNotification.setStatus(_B)
h3cResMonMinorRecoverNotification=NotificationType((1,3,6,1,4,1,2011,10,2,169,3,0,2))
h3cResMonMinorRecoverNotification.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:h3cResMonMinorRecoverNotification.setStatus(_B)
h3cResMonSevereNotification=NotificationType((1,3,6,1,4,1,2011,10,2,169,3,0,3))
h3cResMonSevereNotification.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:h3cResMonSevereNotification.setStatus(_B)
h3cResMonSevereRecoverNotification=NotificationType((1,3,6,1,4,1,2011,10,2,169,3,0,4))
h3cResMonSevereRecoverNotification.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:h3cResMonSevereRecoverNotification.setStatus(_B)
h3cResMonUsedUpNotification=NotificationType((1,3,6,1,4,1,2011,10,2,169,3,0,5))
h3cResMonUsedUpNotification.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:h3cResMonUsedUpNotification.setStatus(_B)
h3cResMonUsedUpRecoverNotification=NotificationType((1,3,6,1,4,1,2011,10,2,169,3,0,6))
h3cResMonUsedUpRecoverNotification.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:h3cResMonUsedUpRecoverNotification.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'h3cResMon':h3cResMon,'h3cResMonScalarObjects':h3cResMonScalarObjects,'h3cResMonMinorResendEnable':h3cResMonMinorResendEnable,'h3cResMonOutputEnable':h3cResMonOutputEnable,'h3cResMonTables':h3cResMonTables,'h3cResMonConfigTable':h3cResMonConfigTable,'h3cResMonConfigEntry':h3cResMonConfigEntry,_C:h3cResMonChassisIndex,_D:h3cResMonSlotIndex,_E:h3cResMonCpuIndex,_F:h3cResMonResourceName,_H:h3cResMonThresholdUnit,_I:h3cResMonMinorThreshold,_J:h3cResMonSevereThreshold,'h3cResMonInfoTable':h3cResMonInfoTable,'h3cResMonInfoEntry':h3cResMonInfoEntry,'h3cResMonUnit':h3cResMonUnit,_K:h3cResMonCurrent,_L:h3cResMonFree,_M:h3cResMonTotal,'h3cResMonNotification':h3cResMonNotification,'h3cResMonTrapPrefix':h3cResMonTrapPrefix,'h3cResMonMinorNotification':h3cResMonMinorNotification,'h3cResMonMinorRecoverNotification':h3cResMonMinorRecoverNotification,'h3cResMonSevereNotification':h3cResMonSevereNotification,'h3cResMonSevereRecoverNotification':h3cResMonSevereRecoverNotification,'h3cResMonUsedUpNotification':h3cResMonUsedUpNotification,'h3cResMonUsedUpRecoverNotification':h3cResMonUsedUpRecoverNotification,'h3cResMonTrapInfor':h3cResMonTrapInfor,_N:h3cResMonAdditionalInfo})