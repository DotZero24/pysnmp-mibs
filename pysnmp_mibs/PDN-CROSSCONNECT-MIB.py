_H='devSyncDataPortAssignIndex'
_G='devDs1FracNumber'
_F='devDs1FracIndex'
_E='read-only'
_D='PDN-CROSSCONNECT-MIB'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
crossConnect,=mibBuilder.importSymbols('PDN-HEADER-MIB','crossConnect')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_DevDs1FracTable_Object=MibTable
devDs1FracTable=_DevDs1FracTable_Object((1,3,6,1,4,1,1795,2,24,2,6,7,1))
if mibBuilder.loadTexts:devDs1FracTable.setStatus(_A)
_DevDs1FracEntry_Object=MibTableRow
devDs1FracEntry=_DevDs1FracEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,7,1,1))
devDs1FracEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:devDs1FracEntry.setStatus(_A)
_DevDs1FracIndex_Type=Integer32
_DevDs1FracIndex_Object=MibTableColumn
devDs1FracIndex=_DevDs1FracIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,7,1,1,1),_DevDs1FracIndex_Type())
devDs1FracIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:devDs1FracIndex.setStatus(_A)
class _DevDs1FracNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_DevDs1FracNumber_Type.__name__=_B
_DevDs1FracNumber_Object=MibTableColumn
devDs1FracNumber=_DevDs1FracNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,7,1,1,2),_DevDs1FracNumber_Type())
devDs1FracNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:devDs1FracNumber.setStatus(_A)
_DevDs1FracIfIndex_Type=Integer32
_DevDs1FracIfIndex_Object=MibTableColumn
devDs1FracIfIndex=_DevDs1FracIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,7,1,1,3),_DevDs1FracIfIndex_Type())
devDs1FracIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:devDs1FracIfIndex.setStatus(_A)
class _DevDs1FracIfFracNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_DevDs1FracIfFracNumber_Type.__name__=_B
_DevDs1FracIfFracNumber_Object=MibTableColumn
devDs1FracIfFracNumber=_DevDs1FracIfFracNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,7,1,1,4),_DevDs1FracIfFracNumber_Type())
devDs1FracIfFracNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:devDs1FracIfFracNumber.setStatus(_A)
_DevSyncDataPortAssignTable_Object=MibTable
devSyncDataPortAssignTable=_DevSyncDataPortAssignTable_Object((1,3,6,1,4,1,1795,2,24,2,6,7,2))
if mibBuilder.loadTexts:devSyncDataPortAssignTable.setStatus(_A)
_DevSyncDataPortAssignEntry_Object=MibTableRow
devSyncDataPortAssignEntry=_DevSyncDataPortAssignEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,7,2,1))
devSyncDataPortAssignEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:devSyncDataPortAssignEntry.setStatus(_A)
_DevSyncDataPortAssignIndex_Type=Integer32
_DevSyncDataPortAssignIndex_Object=MibTableColumn
devSyncDataPortAssignIndex=_DevSyncDataPortAssignIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,7,2,1,1),_DevSyncDataPortAssignIndex_Type())
devSyncDataPortAssignIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:devSyncDataPortAssignIndex.setStatus(_A)
class _DevSyncDataPortAssignRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('rate56or64',1),('rate112or128',2),('rate168or192',3),('rate224or256',4),('rate280or320',5),('rate336or384',6),('rate392or448',7),('rate448or512',8),('rate504or576',9),('rate560or640',10),('rate616or704',11),('rate672or768',12),('rate728or832',13),('rate784or896',14),('rate840or960',15),('rate896or1024',16),('rate952or1088',17),('rate1008or1152',18),('rate1064or1216',19),('rate1120or1280',20),('rate1176or1344',21),('rate1232or1408',22),('rate1288or1472',23),('rate1344or1536',24)))
_DevSyncDataPortAssignRate_Type.__name__=_B
_DevSyncDataPortAssignRate_Object=MibTableColumn
devSyncDataPortAssignRate=_DevSyncDataPortAssignRate_Object((1,3,6,1,4,1,1795,2,24,2,6,7,2,1,2),_DevSyncDataPortAssignRate_Type())
devSyncDataPortAssignRate.setMaxAccess(_C)
if mibBuilder.loadTexts:devSyncDataPortAssignRate.setStatus(_A)
_DevSyncDataPortAssignIfIndex_Type=Integer32
_DevSyncDataPortAssignIfIndex_Object=MibTableColumn
devSyncDataPortAssignIfIndex=_DevSyncDataPortAssignIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,7,2,1,3),_DevSyncDataPortAssignIfIndex_Type())
devSyncDataPortAssignIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:devSyncDataPortAssignIfIndex.setStatus(_A)
_DevCrossConUtility_ObjectIdentity=ObjectIdentity
devCrossConUtility=_DevCrossConUtility_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,7,4))
class _DevCrossConClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('inprogress',2),('clear',3)))
_DevCrossConClear_Type.__name__=_B
_DevCrossConClear_Object=MibScalar
devCrossConClear=_DevCrossConClear_Object((1,3,6,1,4,1,1795,2,24,2,6,7,4,1),_DevCrossConClear_Type())
devCrossConClear.setMaxAccess(_C)
if mibBuilder.loadTexts:devCrossConClear.setStatus(_A)
_DevCrossConTableLastChange_Type=TimeTicks
_DevCrossConTableLastChange_Object=MibScalar
devCrossConTableLastChange=_DevCrossConTableLastChange_Object((1,3,6,1,4,1,1795,2,24,2,6,7,4,2),_DevCrossConTableLastChange_Type())
devCrossConTableLastChange.setMaxAccess(_E)
if mibBuilder.loadTexts:devCrossConTableLastChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'devDs1FracTable':devDs1FracTable,'devDs1FracEntry':devDs1FracEntry,_F:devDs1FracIndex,_G:devDs1FracNumber,'devDs1FracIfIndex':devDs1FracIfIndex,'devDs1FracIfFracNumber':devDs1FracIfFracNumber,'devSyncDataPortAssignTable':devSyncDataPortAssignTable,'devSyncDataPortAssignEntry':devSyncDataPortAssignEntry,_H:devSyncDataPortAssignIndex,'devSyncDataPortAssignRate':devSyncDataPortAssignRate,'devSyncDataPortAssignIfIndex':devSyncDataPortAssignIfIndex,'devCrossConUtility':devCrossConUtility,'devCrossConClear':devCrossConClear,'devCrossConTableLastChange':devCrossConTableLastChange})