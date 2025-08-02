_L='bsSourceGuardStatsIfIndex'
_K='bsSourceGuardAddrMACAddr'
_J='bsSourceGuardAddrAddress'
_I='bsSourceGuardAddrType'
_H='bsSourceGuardAddrIndex'
_G='bsSourceGuardConfigIfIndex'
_F='bsSourceGuardConfigMode'
_E='read-only'
_D='Integer32'
_C='not-accessible'
_B='BAY-STACK-SOURCE-GUARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackSourceGuardMib=ModuleIdentity((1,3,6,1,4,1,45,5,20))
if mibBuilder.loadTexts:bayStackSourceGuardMib.setRevisions(('2020-11-12 00:00','2020-11-02 00:00','2008-10-30 00:00','2008-03-31 00:00','2007-05-07 00:00','2007-03-23 00:00'))
_BsSourceGuardNotifications_ObjectIdentity=ObjectIdentity
bsSourceGuardNotifications=_BsSourceGuardNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,20,0))
_BsSourceGuardObjects_ObjectIdentity=ObjectIdentity
bsSourceGuardObjects=_BsSourceGuardObjects_ObjectIdentity((1,3,6,1,4,1,45,5,20,1))
_BsSourceGuardConfigTable_Object=MibTable
bsSourceGuardConfigTable=_BsSourceGuardConfigTable_Object((1,3,6,1,4,1,45,5,20,1,1))
if mibBuilder.loadTexts:bsSourceGuardConfigTable.setStatus(_A)
_BsSourceGuardConfigEntry_Object=MibTableRow
bsSourceGuardConfigEntry=_BsSourceGuardConfigEntry_Object((1,3,6,1,4,1,45,5,20,1,1,1))
bsSourceGuardConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:bsSourceGuardConfigEntry.setStatus(_A)
_BsSourceGuardConfigIfIndex_Type=InterfaceIndex
_BsSourceGuardConfigIfIndex_Object=MibTableColumn
bsSourceGuardConfigIfIndex=_BsSourceGuardConfigIfIndex_Object((1,3,6,1,4,1,45,5,20,1,1,1,1),_BsSourceGuardConfigIfIndex_Type())
bsSourceGuardConfigIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:bsSourceGuardConfigIfIndex.setStatus(_A)
class _BsSourceGuardConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('ip',2)))
_BsSourceGuardConfigMode_Type.__name__=_D
_BsSourceGuardConfigMode_Object=MibTableColumn
bsSourceGuardConfigMode=_BsSourceGuardConfigMode_Object((1,3,6,1,4,1,45,5,20,1,1,1,2),_BsSourceGuardConfigMode_Type())
bsSourceGuardConfigMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:bsSourceGuardConfigMode.setStatus(_A)
class _BsSourceGuardOrigin_Type(Bits):namedValues=NamedValues(*(('config',0),('radius',1)))
_BsSourceGuardOrigin_Type.__name__='Bits'
_BsSourceGuardOrigin_Object=MibTableColumn
bsSourceGuardOrigin=_BsSourceGuardOrigin_Object((1,3,6,1,4,1,45,5,20,1,1,1,3),_BsSourceGuardOrigin_Type())
bsSourceGuardOrigin.setMaxAccess(_E)
if mibBuilder.loadTexts:bsSourceGuardOrigin.setStatus(_A)
_BsSourceGuardAddrTable_Object=MibTable
bsSourceGuardAddrTable=_BsSourceGuardAddrTable_Object((1,3,6,1,4,1,45,5,20,1,2))
if mibBuilder.loadTexts:bsSourceGuardAddrTable.setStatus(_A)
_BsSourceGuardAddrEntry_Object=MibTableRow
bsSourceGuardAddrEntry=_BsSourceGuardAddrEntry_Object((1,3,6,1,4,1,45,5,20,1,2,1))
bsSourceGuardAddrEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:bsSourceGuardAddrEntry.setStatus(_A)
_BsSourceGuardAddrIndex_Type=InterfaceIndex
_BsSourceGuardAddrIndex_Object=MibTableColumn
bsSourceGuardAddrIndex=_BsSourceGuardAddrIndex_Object((1,3,6,1,4,1,45,5,20,1,2,1,1),_BsSourceGuardAddrIndex_Type())
bsSourceGuardAddrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:bsSourceGuardAddrIndex.setStatus(_A)
_BsSourceGuardAddrType_Type=InetAddressType
_BsSourceGuardAddrType_Object=MibTableColumn
bsSourceGuardAddrType=_BsSourceGuardAddrType_Object((1,3,6,1,4,1,45,5,20,1,2,1,2),_BsSourceGuardAddrType_Type())
bsSourceGuardAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsSourceGuardAddrType.setStatus(_A)
_BsSourceGuardAddrAddress_Type=InetAddress
_BsSourceGuardAddrAddress_Object=MibTableColumn
bsSourceGuardAddrAddress=_BsSourceGuardAddrAddress_Object((1,3,6,1,4,1,45,5,20,1,2,1,3),_BsSourceGuardAddrAddress_Type())
bsSourceGuardAddrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsSourceGuardAddrAddress.setStatus(_A)
_BsSourceGuardAddrMACAddr_Type=MacAddress
_BsSourceGuardAddrMACAddr_Object=MibTableColumn
bsSourceGuardAddrMACAddr=_BsSourceGuardAddrMACAddr_Object((1,3,6,1,4,1,45,5,20,1,2,1,4),_BsSourceGuardAddrMACAddr_Type())
bsSourceGuardAddrMACAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bsSourceGuardAddrMACAddr.setStatus(_A)
class _BsSourceGuardAddrSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('dhcpSnooping',1))
_BsSourceGuardAddrSource_Type.__name__=_D
_BsSourceGuardAddrSource_Object=MibTableColumn
bsSourceGuardAddrSource=_BsSourceGuardAddrSource_Object((1,3,6,1,4,1,45,5,20,1,2,1,5),_BsSourceGuardAddrSource_Type())
bsSourceGuardAddrSource.setMaxAccess(_E)
if mibBuilder.loadTexts:bsSourceGuardAddrSource.setStatus(_A)
_BsSourceGuardStatsTable_Object=MibTable
bsSourceGuardStatsTable=_BsSourceGuardStatsTable_Object((1,3,6,1,4,1,45,5,20,1,3))
if mibBuilder.loadTexts:bsSourceGuardStatsTable.setStatus(_A)
_BsSourceGuardStatsEntry_Object=MibTableRow
bsSourceGuardStatsEntry=_BsSourceGuardStatsEntry_Object((1,3,6,1,4,1,45,5,20,1,3,1))
bsSourceGuardStatsEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:bsSourceGuardStatsEntry.setStatus(_A)
_BsSourceGuardStatsIfIndex_Type=InterfaceIndex
_BsSourceGuardStatsIfIndex_Object=MibTableColumn
bsSourceGuardStatsIfIndex=_BsSourceGuardStatsIfIndex_Object((1,3,6,1,4,1,45,5,20,1,3,1,1),_BsSourceGuardStatsIfIndex_Type())
bsSourceGuardStatsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:bsSourceGuardStatsIfIndex.setStatus(_A)
_BsSourceGuardStatsDroppedPackets_Type=Counter32
_BsSourceGuardStatsDroppedPackets_Object=MibTableColumn
bsSourceGuardStatsDroppedPackets=_BsSourceGuardStatsDroppedPackets_Object((1,3,6,1,4,1,45,5,20,1,3,1,2),_BsSourceGuardStatsDroppedPackets_Type())
bsSourceGuardStatsDroppedPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:bsSourceGuardStatsDroppedPackets.setStatus(_A)
bsSourceGuardReachedMaxIpEntries=NotificationType((1,3,6,1,4,1,45,5,20,0,1))
bsSourceGuardReachedMaxIpEntries.setObjects((_B,_F))
if mibBuilder.loadTexts:bsSourceGuardReachedMaxIpEntries.setStatus(_A)
bsSourceGuardCannotEnablePort=NotificationType((1,3,6,1,4,1,45,5,20,0,2))
bsSourceGuardCannotEnablePort.setObjects((_B,_F))
if mibBuilder.loadTexts:bsSourceGuardCannotEnablePort.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bayStackSourceGuardMib':bayStackSourceGuardMib,'bsSourceGuardNotifications':bsSourceGuardNotifications,'bsSourceGuardReachedMaxIpEntries':bsSourceGuardReachedMaxIpEntries,'bsSourceGuardCannotEnablePort':bsSourceGuardCannotEnablePort,'bsSourceGuardObjects':bsSourceGuardObjects,'bsSourceGuardConfigTable':bsSourceGuardConfigTable,'bsSourceGuardConfigEntry':bsSourceGuardConfigEntry,_G:bsSourceGuardConfigIfIndex,_F:bsSourceGuardConfigMode,'bsSourceGuardOrigin':bsSourceGuardOrigin,'bsSourceGuardAddrTable':bsSourceGuardAddrTable,'bsSourceGuardAddrEntry':bsSourceGuardAddrEntry,_H:bsSourceGuardAddrIndex,_I:bsSourceGuardAddrType,_J:bsSourceGuardAddrAddress,_K:bsSourceGuardAddrMACAddr,'bsSourceGuardAddrSource':bsSourceGuardAddrSource,'bsSourceGuardStatsTable':bsSourceGuardStatsTable,'bsSourceGuardStatsEntry':bsSourceGuardStatsEntry,_L:bsSourceGuardStatsIfIndex,'bsSourceGuardStatsDroppedPackets':bsSourceGuardStatsDroppedPackets})