_O='bsmfVlanAllowedInetAddress'
_N='bsmfVlanAllowedInetAddressType'
_M='bsmfVlanAllowedInetAddressVlanId'
_L='bsmfVlanAllowedAddressMacAddr'
_K='bsmfVlanAllowedAddressVlanId'
_J='bsmfVlanId'
_I='bsmfAllowedInetAddress'
_H='bsmfAllowedInetAddressType'
_G='bsmfAllowedAddressMacAddr'
_F='read-write'
_E='InetAddress'
_D='read-create'
_C='not-accessible'
_B='BAY-STACK-MULTICAST-FLOODING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E,'InetAddressType')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackMulticastFloodingMib=ModuleIdentity((1,3,6,1,4,1,45,5,6))
if mibBuilder.loadTexts:bayStackMulticastFloodingMib.setRevisions(('2009-06-25 00:00','2008-06-25 00:00','2008-06-19 00:00','2006-08-07 00:00','2004-05-19 00:00'))
_BsmfNotifications_ObjectIdentity=ObjectIdentity
bsmfNotifications=_BsmfNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,6,0))
_BsmfObjects_ObjectIdentity=ObjectIdentity
bsmfObjects=_BsmfObjects_ObjectIdentity((1,3,6,1,4,1,45,5,6,1))
_BsmfMulticastFloodingEnabled_Type=TruthValue
_BsmfMulticastFloodingEnabled_Object=MibScalar
bsmfMulticastFloodingEnabled=_BsmfMulticastFloodingEnabled_Object((1,3,6,1,4,1,45,5,6,1,1),_BsmfMulticastFloodingEnabled_Type())
bsmfMulticastFloodingEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:bsmfMulticastFloodingEnabled.setStatus(_A)
_BsmfAllowedAddressTable_Object=MibTable
bsmfAllowedAddressTable=_BsmfAllowedAddressTable_Object((1,3,6,1,4,1,45,5,6,2))
if mibBuilder.loadTexts:bsmfAllowedAddressTable.setStatus(_A)
_BsmfAllowedAddressEntry_Object=MibTableRow
bsmfAllowedAddressEntry=_BsmfAllowedAddressEntry_Object((1,3,6,1,4,1,45,5,6,2,1))
bsmfAllowedAddressEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:bsmfAllowedAddressEntry.setStatus(_A)
_BsmfAllowedAddressMacAddr_Type=MacAddress
_BsmfAllowedAddressMacAddr_Object=MibTableColumn
bsmfAllowedAddressMacAddr=_BsmfAllowedAddressMacAddr_Object((1,3,6,1,4,1,45,5,6,2,1,1),_BsmfAllowedAddressMacAddr_Type())
bsmfAllowedAddressMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bsmfAllowedAddressMacAddr.setStatus(_A)
_BsmfAllowedAddressRowStatus_Type=RowStatus
_BsmfAllowedAddressRowStatus_Object=MibTableColumn
bsmfAllowedAddressRowStatus=_BsmfAllowedAddressRowStatus_Object((1,3,6,1,4,1,45,5,6,2,1,2),_BsmfAllowedAddressRowStatus_Type())
bsmfAllowedAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bsmfAllowedAddressRowStatus.setStatus(_A)
_BsmfAllowedInetAddressTable_Object=MibTable
bsmfAllowedInetAddressTable=_BsmfAllowedInetAddressTable_Object((1,3,6,1,4,1,45,5,6,3))
if mibBuilder.loadTexts:bsmfAllowedInetAddressTable.setStatus(_A)
_BsmfAllowedInetAddressEntry_Object=MibTableRow
bsmfAllowedInetAddressEntry=_BsmfAllowedInetAddressEntry_Object((1,3,6,1,4,1,45,5,6,3,1))
bsmfAllowedInetAddressEntry.setIndexNames((0,_B,_H),(1,_B,_I))
if mibBuilder.loadTexts:bsmfAllowedInetAddressEntry.setStatus(_A)
_BsmfAllowedInetAddressType_Type=InetAddressType
_BsmfAllowedInetAddressType_Object=MibTableColumn
bsmfAllowedInetAddressType=_BsmfAllowedInetAddressType_Object((1,3,6,1,4,1,45,5,6,3,1,1),_BsmfAllowedInetAddressType_Type())
bsmfAllowedInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsmfAllowedInetAddressType.setStatus(_A)
class _BsmfAllowedInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_BsmfAllowedInetAddress_Type.__name__=_E
_BsmfAllowedInetAddress_Object=MibTableColumn
bsmfAllowedInetAddress=_BsmfAllowedInetAddress_Object((1,3,6,1,4,1,45,5,6,3,1,2),_BsmfAllowedInetAddress_Type())
bsmfAllowedInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsmfAllowedInetAddress.setStatus(_A)
_BsmfAllowedInetAddressRowStatus_Type=RowStatus
_BsmfAllowedInetAddressRowStatus_Object=MibTableColumn
bsmfAllowedInetAddressRowStatus=_BsmfAllowedInetAddressRowStatus_Object((1,3,6,1,4,1,45,5,6,3,1,3),_BsmfAllowedInetAddressRowStatus_Type())
bsmfAllowedInetAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bsmfAllowedInetAddressRowStatus.setStatus(_A)
_BsmfVlanTable_Object=MibTable
bsmfVlanTable=_BsmfVlanTable_Object((1,3,6,1,4,1,45,5,6,4))
if mibBuilder.loadTexts:bsmfVlanTable.setStatus(_A)
_BsmfVlanEntry_Object=MibTableRow
bsmfVlanEntry=_BsmfVlanEntry_Object((1,3,6,1,4,1,45,5,6,4,1))
bsmfVlanEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:bsmfVlanEntry.setStatus(_A)
_BsmfVlanId_Type=VlanId
_BsmfVlanId_Object=MibTableColumn
bsmfVlanId=_BsmfVlanId_Object((1,3,6,1,4,1,45,5,6,4,1,1),_BsmfVlanId_Type())
bsmfVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:bsmfVlanId.setStatus(_A)
_BsmfVlanMulticastFloodingEnabled_Type=TruthValue
_BsmfVlanMulticastFloodingEnabled_Object=MibTableColumn
bsmfVlanMulticastFloodingEnabled=_BsmfVlanMulticastFloodingEnabled_Object((1,3,6,1,4,1,45,5,6,4,1,2),_BsmfVlanMulticastFloodingEnabled_Type())
bsmfVlanMulticastFloodingEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:bsmfVlanMulticastFloodingEnabled.setStatus(_A)
_BsmfVlanAllowedAddressTable_Object=MibTable
bsmfVlanAllowedAddressTable=_BsmfVlanAllowedAddressTable_Object((1,3,6,1,4,1,45,5,6,5))
if mibBuilder.loadTexts:bsmfVlanAllowedAddressTable.setStatus(_A)
_BsmfVlanAllowedAddressEntry_Object=MibTableRow
bsmfVlanAllowedAddressEntry=_BsmfVlanAllowedAddressEntry_Object((1,3,6,1,4,1,45,5,6,5,1))
bsmfVlanAllowedAddressEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:bsmfVlanAllowedAddressEntry.setStatus(_A)
_BsmfVlanAllowedAddressVlanId_Type=VlanId
_BsmfVlanAllowedAddressVlanId_Object=MibTableColumn
bsmfVlanAllowedAddressVlanId=_BsmfVlanAllowedAddressVlanId_Object((1,3,6,1,4,1,45,5,6,5,1,1),_BsmfVlanAllowedAddressVlanId_Type())
bsmfVlanAllowedAddressVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:bsmfVlanAllowedAddressVlanId.setStatus(_A)
_BsmfVlanAllowedAddressMacAddr_Type=MacAddress
_BsmfVlanAllowedAddressMacAddr_Object=MibTableColumn
bsmfVlanAllowedAddressMacAddr=_BsmfVlanAllowedAddressMacAddr_Object((1,3,6,1,4,1,45,5,6,5,1,2),_BsmfVlanAllowedAddressMacAddr_Type())
bsmfVlanAllowedAddressMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bsmfVlanAllowedAddressMacAddr.setStatus(_A)
_BsmfVlanAllowedAddressRowStatus_Type=RowStatus
_BsmfVlanAllowedAddressRowStatus_Object=MibTableColumn
bsmfVlanAllowedAddressRowStatus=_BsmfVlanAllowedAddressRowStatus_Object((1,3,6,1,4,1,45,5,6,5,1,3),_BsmfVlanAllowedAddressRowStatus_Type())
bsmfVlanAllowedAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bsmfVlanAllowedAddressRowStatus.setStatus(_A)
_BsmfVlanAllowedInetAddressTable_Object=MibTable
bsmfVlanAllowedInetAddressTable=_BsmfVlanAllowedInetAddressTable_Object((1,3,6,1,4,1,45,5,6,6))
if mibBuilder.loadTexts:bsmfVlanAllowedInetAddressTable.setStatus(_A)
_BsmfVlanAllowedInetAddressEntry_Object=MibTableRow
bsmfVlanAllowedInetAddressEntry=_BsmfVlanAllowedInetAddressEntry_Object((1,3,6,1,4,1,45,5,6,6,1))
bsmfVlanAllowedInetAddressEntry.setIndexNames((0,_B,_M),(0,_B,_N),(1,_B,_O))
if mibBuilder.loadTexts:bsmfVlanAllowedInetAddressEntry.setStatus(_A)
_BsmfVlanAllowedInetAddressVlanId_Type=VlanId
_BsmfVlanAllowedInetAddressVlanId_Object=MibTableColumn
bsmfVlanAllowedInetAddressVlanId=_BsmfVlanAllowedInetAddressVlanId_Object((1,3,6,1,4,1,45,5,6,6,1,1),_BsmfVlanAllowedInetAddressVlanId_Type())
bsmfVlanAllowedInetAddressVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:bsmfVlanAllowedInetAddressVlanId.setStatus(_A)
_BsmfVlanAllowedInetAddressType_Type=InetAddressType
_BsmfVlanAllowedInetAddressType_Object=MibTableColumn
bsmfVlanAllowedInetAddressType=_BsmfVlanAllowedInetAddressType_Object((1,3,6,1,4,1,45,5,6,6,1,2),_BsmfVlanAllowedInetAddressType_Type())
bsmfVlanAllowedInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsmfVlanAllowedInetAddressType.setStatus(_A)
class _BsmfVlanAllowedInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_BsmfVlanAllowedInetAddress_Type.__name__=_E
_BsmfVlanAllowedInetAddress_Object=MibTableColumn
bsmfVlanAllowedInetAddress=_BsmfVlanAllowedInetAddress_Object((1,3,6,1,4,1,45,5,6,6,1,3),_BsmfVlanAllowedInetAddress_Type())
bsmfVlanAllowedInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsmfVlanAllowedInetAddress.setStatus(_A)
_BsmfVlanAllowedInetAddressRowStatus_Type=RowStatus
_BsmfVlanAllowedInetAddressRowStatus_Object=MibTableColumn
bsmfVlanAllowedInetAddressRowStatus=_BsmfVlanAllowedInetAddressRowStatus_Object((1,3,6,1,4,1,45,5,6,6,1,4),_BsmfVlanAllowedInetAddressRowStatus_Type())
bsmfVlanAllowedInetAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bsmfVlanAllowedInetAddressRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bayStackMulticastFloodingMib':bayStackMulticastFloodingMib,'bsmfNotifications':bsmfNotifications,'bsmfObjects':bsmfObjects,'bsmfMulticastFloodingEnabled':bsmfMulticastFloodingEnabled,'bsmfAllowedAddressTable':bsmfAllowedAddressTable,'bsmfAllowedAddressEntry':bsmfAllowedAddressEntry,_G:bsmfAllowedAddressMacAddr,'bsmfAllowedAddressRowStatus':bsmfAllowedAddressRowStatus,'bsmfAllowedInetAddressTable':bsmfAllowedInetAddressTable,'bsmfAllowedInetAddressEntry':bsmfAllowedInetAddressEntry,_H:bsmfAllowedInetAddressType,_I:bsmfAllowedInetAddress,'bsmfAllowedInetAddressRowStatus':bsmfAllowedInetAddressRowStatus,'bsmfVlanTable':bsmfVlanTable,'bsmfVlanEntry':bsmfVlanEntry,_J:bsmfVlanId,'bsmfVlanMulticastFloodingEnabled':bsmfVlanMulticastFloodingEnabled,'bsmfVlanAllowedAddressTable':bsmfVlanAllowedAddressTable,'bsmfVlanAllowedAddressEntry':bsmfVlanAllowedAddressEntry,_K:bsmfVlanAllowedAddressVlanId,_L:bsmfVlanAllowedAddressMacAddr,'bsmfVlanAllowedAddressRowStatus':bsmfVlanAllowedAddressRowStatus,'bsmfVlanAllowedInetAddressTable':bsmfVlanAllowedInetAddressTable,'bsmfVlanAllowedInetAddressEntry':bsmfVlanAllowedInetAddressEntry,_M:bsmfVlanAllowedInetAddressVlanId,_N:bsmfVlanAllowedInetAddressType,_O:bsmfVlanAllowedInetAddress,'bsmfVlanAllowedInetAddressRowStatus':bsmfVlanAllowedInetAddressRowStatus})