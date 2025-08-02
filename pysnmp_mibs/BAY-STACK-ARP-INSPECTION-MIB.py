_H='bsArpInspectionNotificationSourceMACAddr'
_G='bsArpInspectionIfTrusted'
_F='bsArpInspectionIfIndex'
_E='read-write'
_D='not-accessible'
_C='bsArpInspectionVlanId'
_B='BAY-STACK-ARP-INSPECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackArpInspectionMib=ModuleIdentity((1,3,6,1,4,1,45,5,18))
if mibBuilder.loadTexts:bayStackArpInspectionMib.setRevisions(('2020-11-12 00:00','2013-10-11 00:00','2013-07-05 00:00','2008-10-30 00:00','2006-06-23 00:00'))
_BsArpInspectionNotifications_ObjectIdentity=ObjectIdentity
bsArpInspectionNotifications=_BsArpInspectionNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,18,0))
_BsArpInspectionObjects_ObjectIdentity=ObjectIdentity
bsArpInspectionObjects=_BsArpInspectionObjects_ObjectIdentity((1,3,6,1,4,1,45,5,18,1))
_BsArpInspectionVlanTable_Object=MibTable
bsArpInspectionVlanTable=_BsArpInspectionVlanTable_Object((1,3,6,1,4,1,45,5,18,1,1))
if mibBuilder.loadTexts:bsArpInspectionVlanTable.setStatus(_A)
_BsArpInspectionVlanEntry_Object=MibTableRow
bsArpInspectionVlanEntry=_BsArpInspectionVlanEntry_Object((1,3,6,1,4,1,45,5,18,1,1,1))
bsArpInspectionVlanEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:bsArpInspectionVlanEntry.setStatus(_A)
_BsArpInspectionVlanId_Type=VlanIndex
_BsArpInspectionVlanId_Object=MibTableColumn
bsArpInspectionVlanId=_BsArpInspectionVlanId_Object((1,3,6,1,4,1,45,5,18,1,1,1,1),_BsArpInspectionVlanId_Type())
bsArpInspectionVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:bsArpInspectionVlanId.setStatus(_A)
_BsArpInspectionVlanEnabled_Type=TruthValue
_BsArpInspectionVlanEnabled_Object=MibTableColumn
bsArpInspectionVlanEnabled=_BsArpInspectionVlanEnabled_Object((1,3,6,1,4,1,45,5,18,1,1,1,2),_BsArpInspectionVlanEnabled_Type())
bsArpInspectionVlanEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:bsArpInspectionVlanEnabled.setStatus(_A)
class _BsArpInspectionOrigin_Type(Bits):namedValues=NamedValues(*(('config',0),('radius',1)))
_BsArpInspectionOrigin_Type.__name__='Bits'
_BsArpInspectionOrigin_Object=MibTableColumn
bsArpInspectionOrigin=_BsArpInspectionOrigin_Object((1,3,6,1,4,1,45,5,18,1,1,1,3),_BsArpInspectionOrigin_Type())
bsArpInspectionOrigin.setMaxAccess('read-only')
if mibBuilder.loadTexts:bsArpInspectionOrigin.setStatus(_A)
_BsArpInspectionIfTable_Object=MibTable
bsArpInspectionIfTable=_BsArpInspectionIfTable_Object((1,3,6,1,4,1,45,5,18,1,2))
if mibBuilder.loadTexts:bsArpInspectionIfTable.setStatus(_A)
_BsArpInspectionIfEntry_Object=MibTableRow
bsArpInspectionIfEntry=_BsArpInspectionIfEntry_Object((1,3,6,1,4,1,45,5,18,1,2,1))
bsArpInspectionIfEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:bsArpInspectionIfEntry.setStatus(_A)
_BsArpInspectionIfIndex_Type=InterfaceIndex
_BsArpInspectionIfIndex_Object=MibTableColumn
bsArpInspectionIfIndex=_BsArpInspectionIfIndex_Object((1,3,6,1,4,1,45,5,18,1,2,1,1),_BsArpInspectionIfIndex_Type())
bsArpInspectionIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bsArpInspectionIfIndex.setStatus(_A)
_BsArpInspectionIfTrusted_Type=TruthValue
_BsArpInspectionIfTrusted_Object=MibTableColumn
bsArpInspectionIfTrusted=_BsArpInspectionIfTrusted_Object((1,3,6,1,4,1,45,5,18,1,2,1,2),_BsArpInspectionIfTrusted_Type())
bsArpInspectionIfTrusted.setMaxAccess(_E)
if mibBuilder.loadTexts:bsArpInspectionIfTrusted.setStatus(_A)
_BsArpInspectionNotificationObjects_ObjectIdentity=ObjectIdentity
bsArpInspectionNotificationObjects=_BsArpInspectionNotificationObjects_ObjectIdentity((1,3,6,1,4,1,45,5,18,1,3))
_BsArpInspectionNotificationSourceMACAddr_Type=MacAddress
_BsArpInspectionNotificationSourceMACAddr_Object=MibScalar
bsArpInspectionNotificationSourceMACAddr=_BsArpInspectionNotificationSourceMACAddr_Object((1,3,6,1,4,1,45,5,18,1,3,1),_BsArpInspectionNotificationSourceMACAddr_Type())
bsArpInspectionNotificationSourceMACAddr.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:bsArpInspectionNotificationSourceMACAddr.setStatus(_A)
bsaiArpPacketDroppedOnUntrustedPort=NotificationType((1,3,6,1,4,1,45,5,18,0,1))
bsaiArpPacketDroppedOnUntrustedPort.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:bsaiArpPacketDroppedOnUntrustedPort.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bayStackArpInspectionMib':bayStackArpInspectionMib,'bsArpInspectionNotifications':bsArpInspectionNotifications,'bsaiArpPacketDroppedOnUntrustedPort':bsaiArpPacketDroppedOnUntrustedPort,'bsArpInspectionObjects':bsArpInspectionObjects,'bsArpInspectionVlanTable':bsArpInspectionVlanTable,'bsArpInspectionVlanEntry':bsArpInspectionVlanEntry,_C:bsArpInspectionVlanId,'bsArpInspectionVlanEnabled':bsArpInspectionVlanEnabled,'bsArpInspectionOrigin':bsArpInspectionOrigin,'bsArpInspectionIfTable':bsArpInspectionIfTable,'bsArpInspectionIfEntry':bsArpInspectionIfEntry,_F:bsArpInspectionIfIndex,_G:bsArpInspectionIfTrusted,'bsArpInspectionNotificationObjects':bsArpInspectionNotificationObjects,_H:bsArpInspectionNotificationSourceMACAddr})