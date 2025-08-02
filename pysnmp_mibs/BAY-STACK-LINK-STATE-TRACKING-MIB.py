_N='bsLstGroupOperState'
_M='read-only'
_L='TruthValue'
_K='Unsigned32'
_J='bsLstInterfaceStatus'
_I='IdList'
_H='PortList'
_G='bsLstGroupIndex'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='BAY-STACK-LINK-STATE-TRACKING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_L)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackLinkStateTrackingMib=ModuleIdentity((1,3,6,1,4,1,45,5,43))
if mibBuilder.loadTexts:bayStackLinkStateTrackingMib.setRevisions(('2018-09-28 00:00','2017-08-31 00:00','2013-10-11 00:00','2013-02-13 00:00','2012-11-15 00:00','2012-10-17 00:00','2012-09-03 00:00'))
class PortList(TextualConvention,OctetString):status=_A
class IdList(TextualConvention,OctetString):status=_A
_BsLstNotifications_ObjectIdentity=ObjectIdentity
bsLstNotifications=_BsLstNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,43,0))
_BsLstObjects_ObjectIdentity=ObjectIdentity
bsLstObjects=_BsLstObjects_ObjectIdentity((1,3,6,1,4,1,45,5,43,1))
_BsLstScalars_ObjectIdentity=ObjectIdentity
bsLstScalars=_BsLstScalars_ObjectIdentity((1,3,6,1,4,1,45,5,43,1,1))
_BsLstGroupTable_Object=MibTable
bsLstGroupTable=_BsLstGroupTable_Object((1,3,6,1,4,1,45,5,43,1,2))
if mibBuilder.loadTexts:bsLstGroupTable.setStatus(_A)
_BsLstGroupEntry_Object=MibTableRow
bsLstGroupEntry=_BsLstGroupEntry_Object((1,3,6,1,4,1,45,5,43,1,2,1))
bsLstGroupEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:bsLstGroupEntry.setStatus(_A)
class _BsLstGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_BsLstGroupIndex_Type.__name__=_K
_BsLstGroupIndex_Object=MibTableColumn
bsLstGroupIndex=_BsLstGroupIndex_Object((1,3,6,1,4,1,45,5,43,1,2,1,1),_BsLstGroupIndex_Type())
bsLstGroupIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:bsLstGroupIndex.setStatus(_A)
class _BsLstGroupEnabled_Type(TruthValue):defaultValue=2
_BsLstGroupEnabled_Type.__name__=_L
_BsLstGroupEnabled_Object=MibTableColumn
bsLstGroupEnabled=_BsLstGroupEnabled_Object((1,3,6,1,4,1,45,5,43,1,2,1,2),_BsLstGroupEnabled_Type())
bsLstGroupEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLstGroupEnabled.setStatus(_A)
class _BsLstGroupUpstreamPortList_Type(PortList):defaultHexValue=''
_BsLstGroupUpstreamPortList_Type.__name__=_H
_BsLstGroupUpstreamPortList_Object=MibTableColumn
bsLstGroupUpstreamPortList=_BsLstGroupUpstreamPortList_Object((1,3,6,1,4,1,45,5,43,1,2,1,3),_BsLstGroupUpstreamPortList_Type())
bsLstGroupUpstreamPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLstGroupUpstreamPortList.setStatus(_A)
class _BsLstGroupDownstreamPortList_Type(PortList):defaultHexValue=''
_BsLstGroupDownstreamPortList_Type.__name__=_H
_BsLstGroupDownstreamPortList_Object=MibTableColumn
bsLstGroupDownstreamPortList=_BsLstGroupDownstreamPortList_Object((1,3,6,1,4,1,45,5,43,1,2,1,4),_BsLstGroupDownstreamPortList_Type())
bsLstGroupDownstreamPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLstGroupDownstreamPortList.setStatus(_A)
class _BsLstGroupUpstreamMltList_Type(IdList):defaultHexValue=''
_BsLstGroupUpstreamMltList_Type.__name__=_I
_BsLstGroupUpstreamMltList_Object=MibTableColumn
bsLstGroupUpstreamMltList=_BsLstGroupUpstreamMltList_Object((1,3,6,1,4,1,45,5,43,1,2,1,5),_BsLstGroupUpstreamMltList_Type())
bsLstGroupUpstreamMltList.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLstGroupUpstreamMltList.setStatus(_A)
class _BsLstGroupDownstreamMltList_Type(IdList):defaultHexValue=''
_BsLstGroupDownstreamMltList_Type.__name__=_I
_BsLstGroupDownstreamMltList_Object=MibTableColumn
bsLstGroupDownstreamMltList=_BsLstGroupDownstreamMltList_Object((1,3,6,1,4,1,45,5,43,1,2,1,6),_BsLstGroupDownstreamMltList_Type())
bsLstGroupDownstreamMltList.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLstGroupDownstreamMltList.setStatus(_A)
class _BsLstGroupOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('notConfigured',3)))
_BsLstGroupOperState_Type.__name__=_F
_BsLstGroupOperState_Object=MibTableColumn
bsLstGroupOperState=_BsLstGroupOperState_Object((1,3,6,1,4,1,45,5,43,1,2,1,7),_BsLstGroupOperState_Type())
bsLstGroupOperState.setMaxAccess(_M)
if mibBuilder.loadTexts:bsLstGroupOperState.setStatus(_A)
_BsLstNotifObjects_ObjectIdentity=ObjectIdentity
bsLstNotifObjects=_BsLstNotifObjects_ObjectIdentity((1,3,6,1,4,1,45,5,43,1,3))
class _BsLstInterfaceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_BsLstInterfaceStatus_Type.__name__=_F
_BsLstInterfaceStatus_Object=MibScalar
bsLstInterfaceStatus=_BsLstInterfaceStatus_Object((1,3,6,1,4,1,45,5,43,1,3,1),_BsLstInterfaceStatus_Type())
bsLstInterfaceStatus.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:bsLstInterfaceStatus.setStatus(_A)
bsLstInterfaceStatusChanged=NotificationType((1,3,6,1,4,1,45,5,43,0,1))
bsLstInterfaceStatusChanged.setObjects(*((_D,_E),(_B,_J),(_B,_G)))
if mibBuilder.loadTexts:bsLstInterfaceStatusChanged.setStatus(_A)
bsLstGroupOperStateChanged=NotificationType((1,3,6,1,4,1,45,5,43,0,2))
bsLstGroupOperStateChanged.setObjects(*((_D,_E),(_B,_J),(_B,_N)))
if mibBuilder.loadTexts:bsLstGroupOperStateChanged.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:PortList,_I:IdList,'bayStackLinkStateTrackingMib':bayStackLinkStateTrackingMib,'bsLstNotifications':bsLstNotifications,'bsLstInterfaceStatusChanged':bsLstInterfaceStatusChanged,'bsLstGroupOperStateChanged':bsLstGroupOperStateChanged,'bsLstObjects':bsLstObjects,'bsLstScalars':bsLstScalars,'bsLstGroupTable':bsLstGroupTable,'bsLstGroupEntry':bsLstGroupEntry,_G:bsLstGroupIndex,'bsLstGroupEnabled':bsLstGroupEnabled,'bsLstGroupUpstreamPortList':bsLstGroupUpstreamPortList,'bsLstGroupDownstreamPortList':bsLstGroupDownstreamPortList,'bsLstGroupUpstreamMltList':bsLstGroupUpstreamMltList,'bsLstGroupDownstreamMltList':bsLstGroupDownstreamMltList,_N:bsLstGroupOperState,'bsLstNotifObjects':bsLstNotifObjects,_J:bsLstInterfaceStatus})