_O='processing'
_N='swEtherCableDiagPortIndex'
_M='CABLE-DIAG-MIB'
_L='no-cable'
_K='count'
_J='unknown'
_I='crosstalk'
_H='open-short'
_G='short'
_F='open'
_E='ok'
_D='other'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
swCableDiagMIB=ModuleIdentity((1,3,6,1,4,1,171,12,58))
_SwCableDiagCtrl_ObjectIdentity=ObjectIdentity
swCableDiagCtrl=_SwCableDiagCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,58,1))
_SwEtherCableDiagTable_Object=MibTable
swEtherCableDiagTable=_SwEtherCableDiagTable_Object((1,3,6,1,4,1,171,12,58,1,1))
if mibBuilder.loadTexts:swEtherCableDiagTable.setStatus(_A)
_SwEtherCableDiagEntry_Object=MibTableRow
swEtherCableDiagEntry=_SwEtherCableDiagEntry_Object((1,3,6,1,4,1,171,12,58,1,1,1))
swEtherCableDiagEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:swEtherCableDiagEntry.setStatus(_A)
class _SwEtherCableDiagPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwEtherCableDiagPortIndex_Type.__name__=_C
_SwEtherCableDiagPortIndex_Object=MibTableColumn
swEtherCableDiagPortIndex=_SwEtherCableDiagPortIndex_Object((1,3,6,1,4,1,171,12,58,1,1,1,1),_SwEtherCableDiagPortIndex_Type())
swEtherCableDiagPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPortIndex.setStatus(_A)
class _SwEtherCableDiagPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('fastEthernet',0),('gigaEthernet',1),(_D,2)))
_SwEtherCableDiagPortType_Type.__name__=_C
_SwEtherCableDiagPortType_Object=MibTableColumn
swEtherCableDiagPortType=_SwEtherCableDiagPortType_Object((1,3,6,1,4,1,171,12,58,1,1,1,2),_SwEtherCableDiagPortType_Type())
swEtherCableDiagPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPortType.setStatus(_A)
class _SwEtherCableDiagLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('link-down',0),('link-up',1),(_D,2)))
_SwEtherCableDiagLinkStatus_Type.__name__=_C
_SwEtherCableDiagLinkStatus_Object=MibTableColumn
swEtherCableDiagLinkStatus=_SwEtherCableDiagLinkStatus_Object((1,3,6,1,4,1,171,12,58,1,1,1,3),_SwEtherCableDiagLinkStatus_Type())
swEtherCableDiagLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagLinkStatus.setStatus(_A)
class _SwEtherCableDiagPair1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_D,8)))
_SwEtherCableDiagPair1Status_Type.__name__=_C
_SwEtherCableDiagPair1Status_Object=MibTableColumn
swEtherCableDiagPair1Status=_SwEtherCableDiagPair1Status_Object((1,3,6,1,4,1,171,12,58,1,1,1,4),_SwEtherCableDiagPair1Status_Type())
swEtherCableDiagPair1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPair1Status.setStatus(_A)
class _SwEtherCableDiagPair2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_D,8)))
_SwEtherCableDiagPair2Status_Type.__name__=_C
_SwEtherCableDiagPair2Status_Object=MibTableColumn
swEtherCableDiagPair2Status=_SwEtherCableDiagPair2Status_Object((1,3,6,1,4,1,171,12,58,1,1,1,5),_SwEtherCableDiagPair2Status_Type())
swEtherCableDiagPair2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPair2Status.setStatus(_A)
class _SwEtherCableDiagPair3Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_D,8)))
_SwEtherCableDiagPair3Status_Type.__name__=_C
_SwEtherCableDiagPair3Status_Object=MibTableColumn
swEtherCableDiagPair3Status=_SwEtherCableDiagPair3Status_Object((1,3,6,1,4,1,171,12,58,1,1,1,6),_SwEtherCableDiagPair3Status_Type())
swEtherCableDiagPair3Status.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPair3Status.setStatus(_A)
class _SwEtherCableDiagPair4Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6),(_L,7),(_D,8)))
_SwEtherCableDiagPair4Status_Type.__name__=_C
_SwEtherCableDiagPair4Status_Object=MibTableColumn
swEtherCableDiagPair4Status=_SwEtherCableDiagPair4Status_Object((1,3,6,1,4,1,171,12,58,1,1,1,7),_SwEtherCableDiagPair4Status_Type())
swEtherCableDiagPair4Status.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPair4Status.setStatus(_A)
_SwEtherCableDiagPair1Length_Type=Integer32
_SwEtherCableDiagPair1Length_Object=MibTableColumn
swEtherCableDiagPair1Length=_SwEtherCableDiagPair1Length_Object((1,3,6,1,4,1,171,12,58,1,1,1,8),_SwEtherCableDiagPair1Length_Type())
swEtherCableDiagPair1Length.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPair1Length.setStatus(_A)
_SwEtherCableDiagPair2Length_Type=Integer32
_SwEtherCableDiagPair2Length_Object=MibTableColumn
swEtherCableDiagPair2Length=_SwEtherCableDiagPair2Length_Object((1,3,6,1,4,1,171,12,58,1,1,1,9),_SwEtherCableDiagPair2Length_Type())
swEtherCableDiagPair2Length.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPair2Length.setStatus(_A)
_SwEtherCableDiagPair3Length_Type=Integer32
_SwEtherCableDiagPair3Length_Object=MibTableColumn
swEtherCableDiagPair3Length=_SwEtherCableDiagPair3Length_Object((1,3,6,1,4,1,171,12,58,1,1,1,10),_SwEtherCableDiagPair3Length_Type())
swEtherCableDiagPair3Length.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPair3Length.setStatus(_A)
_SwEtherCableDiagPair4Length_Type=Integer32
_SwEtherCableDiagPair4Length_Object=MibTableColumn
swEtherCableDiagPair4Length=_SwEtherCableDiagPair4Length_Object((1,3,6,1,4,1,171,12,58,1,1,1,11),_SwEtherCableDiagPair4Length_Type())
swEtherCableDiagPair4Length.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagPair4Length.setStatus(_A)
class _SwEtherCableDiagAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('action',1),(_O,2),(_D,3)))
_SwEtherCableDiagAction_Type.__name__=_C
_SwEtherCableDiagAction_Object=MibTableColumn
swEtherCableDiagAction=_SwEtherCableDiagAction_Object((1,3,6,1,4,1,171,12,58,1,1,1,12),_SwEtherCableDiagAction_Type())
swEtherCableDiagAction.setMaxAccess('read-write')
if mibBuilder.loadTexts:swEtherCableDiagAction.setStatus(_A)
class _SwEtherCableDiagStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-run',1),(_O,2),('last-test-ok',3),('last-test-failed',4)))
_SwEtherCableDiagStatus_Type.__name__=_C
_SwEtherCableDiagStatus_Object=MibTableColumn
swEtherCableDiagStatus=_SwEtherCableDiagStatus_Object((1,3,6,1,4,1,171,12,58,1,1,1,13),_SwEtherCableDiagStatus_Type())
swEtherCableDiagStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherCableDiagStatus.setStatus(_A)
mibBuilder.exportSymbols(_M,**{'swCableDiagMIB':swCableDiagMIB,'swCableDiagCtrl':swCableDiagCtrl,'swEtherCableDiagTable':swEtherCableDiagTable,'swEtherCableDiagEntry':swEtherCableDiagEntry,_N:swEtherCableDiagPortIndex,'swEtherCableDiagPortType':swEtherCableDiagPortType,'swEtherCableDiagLinkStatus':swEtherCableDiagLinkStatus,'swEtherCableDiagPair1Status':swEtherCableDiagPair1Status,'swEtherCableDiagPair2Status':swEtherCableDiagPair2Status,'swEtherCableDiagPair3Status':swEtherCableDiagPair3Status,'swEtherCableDiagPair4Status':swEtherCableDiagPair4Status,'swEtherCableDiagPair1Length':swEtherCableDiagPair1Length,'swEtherCableDiagPair2Length':swEtherCableDiagPair2Length,'swEtherCableDiagPair3Length':swEtherCableDiagPair3Length,'swEtherCableDiagPair4Length':swEtherCableDiagPair4Length,'swEtherCableDiagAction':swEtherCableDiagAction,'swEtherCableDiagStatus':swEtherCableDiagStatus})