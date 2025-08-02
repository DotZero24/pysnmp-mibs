_J='rldot1qTpFdbEntry'
_I='rldot1qStaticUnicastEntry'
_H='rldot1qTpFdbCountType'
_G='rldot1qTpFdbCountPort'
_F='rldot1qTpFdbCountVlanTag'
_E='learned'
_D='read-only'
_C='Integer32'
_B='CISCOSB-rldot1q-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rlpBridgeMIBObjects,=mibBuilder.importSymbols('CISCOSB-BRIDGEMIBOBJECTS-MIB','rlpBridgeMIBObjects')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
PortList,dot1qStaticUnicastEntry,dot1qTpFdbEntry=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','dot1qStaticUnicastEntry','dot1qTpFdbEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlq_bridge_mib=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,57,8))
if mibBuilder.loadTexts:rlq_bridge_mib.setRevisions(('2008-11-25 00:00',))
_Rldot1q_ObjectIdentity=ObjectIdentity
rldot1q=_Rldot1q_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,57,8))
_Rldot1qStaticUnicastTable_Object=MibTable
rldot1qStaticUnicastTable=_Rldot1qStaticUnicastTable_Object((1,3,6,1,4,1,9,6,1,101,57,8,1))
if mibBuilder.loadTexts:rldot1qStaticUnicastTable.setStatus(_A)
_Rldot1qStaticUnicastEntry_Object=MibTableRow
rldot1qStaticUnicastEntry=_Rldot1qStaticUnicastEntry_Object((1,3,6,1,4,1,9,6,1,101,57,8,1,1))
if mibBuilder.loadTexts:rldot1qStaticUnicastEntry.setStatus(_A)
class _Rldot1qStaticUnicastAddressOwner_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),(_E,2)))
_Rldot1qStaticUnicastAddressOwner_Type.__name__=_C
_Rldot1qStaticUnicastAddressOwner_Object=MibTableColumn
rldot1qStaticUnicastAddressOwner=_Rldot1qStaticUnicastAddressOwner_Object((1,3,6,1,4,1,9,6,1,101,57,8,1,1,1),_Rldot1qStaticUnicastAddressOwner_Type())
rldot1qStaticUnicastAddressOwner.setMaxAccess('read-write')
if mibBuilder.loadTexts:rldot1qStaticUnicastAddressOwner.setStatus(_A)
_Rldot1qTpFdbTable_Object=MibTable
rldot1qTpFdbTable=_Rldot1qTpFdbTable_Object((1,3,6,1,4,1,9,6,1,101,57,8,2))
if mibBuilder.loadTexts:rldot1qTpFdbTable.setStatus(_A)
_Rldot1qTpFdbEntry_Object=MibTableRow
rldot1qTpFdbEntry=_Rldot1qTpFdbEntry_Object((1,3,6,1,4,1,9,6,1,101,57,8,2,1))
if mibBuilder.loadTexts:rldot1qTpFdbEntry.setStatus(_A)
class _Rldot1qTpFdbSubStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('dynamic-static',2)))
_Rldot1qTpFdbSubStatus_Type.__name__=_C
_Rldot1qTpFdbSubStatus_Object=MibTableColumn
rldot1qTpFdbSubStatus=_Rldot1qTpFdbSubStatus_Object((1,3,6,1,4,1,9,6,1,101,57,8,2,1,1),_Rldot1qTpFdbSubStatus_Type())
rldot1qTpFdbSubStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rldot1qTpFdbSubStatus.setStatus(_A)
_Rldot1qTpFdbCountTable_Object=MibTable
rldot1qTpFdbCountTable=_Rldot1qTpFdbCountTable_Object((1,3,6,1,4,1,9,6,1,101,57,8,3))
if mibBuilder.loadTexts:rldot1qTpFdbCountTable.setStatus(_A)
_Rldot1qTpFdbCountEntry_Object=MibTableRow
rldot1qTpFdbCountEntry=_Rldot1qTpFdbCountEntry_Object((1,3,6,1,4,1,9,6,1,101,57,8,3,1))
rldot1qTpFdbCountEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:rldot1qTpFdbCountEntry.setStatus(_A)
class _Rldot1qTpFdbCountVlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Rldot1qTpFdbCountVlanTag_Type.__name__=_C
_Rldot1qTpFdbCountVlanTag_Object=MibTableColumn
rldot1qTpFdbCountVlanTag=_Rldot1qTpFdbCountVlanTag_Object((1,3,6,1,4,1,9,6,1,101,57,8,3,1,1),_Rldot1qTpFdbCountVlanTag_Type())
rldot1qTpFdbCountVlanTag.setMaxAccess(_D)
if mibBuilder.loadTexts:rldot1qTpFdbCountVlanTag.setStatus(_A)
_Rldot1qTpFdbCountPort_Type=Integer32
_Rldot1qTpFdbCountPort_Object=MibTableColumn
rldot1qTpFdbCountPort=_Rldot1qTpFdbCountPort_Object((1,3,6,1,4,1,9,6,1,101,57,8,3,1,2),_Rldot1qTpFdbCountPort_Type())
rldot1qTpFdbCountPort.setMaxAccess(_D)
if mibBuilder.loadTexts:rldot1qTpFdbCountPort.setStatus(_A)
class _Rldot1qTpFdbCountType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('invalid',2),(_E,3),('self',4),('mgmt',5),('multicast',6),('ipv4Host',7),('ipv6Host',8)))
_Rldot1qTpFdbCountType_Type.__name__=_C
_Rldot1qTpFdbCountType_Object=MibTableColumn
rldot1qTpFdbCountType=_Rldot1qTpFdbCountType_Object((1,3,6,1,4,1,9,6,1,101,57,8,3,1,3),_Rldot1qTpFdbCountType_Type())
rldot1qTpFdbCountType.setMaxAccess(_D)
if mibBuilder.loadTexts:rldot1qTpFdbCountType.setStatus(_A)
_Rldot1qTpFdbCountCount_Type=Integer32
_Rldot1qTpFdbCountCount_Object=MibTableColumn
rldot1qTpFdbCountCount=_Rldot1qTpFdbCountCount_Object((1,3,6,1,4,1,9,6,1,101,57,8,3,1,4),_Rldot1qTpFdbCountCount_Type())
rldot1qTpFdbCountCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rldot1qTpFdbCountCount.setStatus(_A)
dot1qStaticUnicastEntry.registerAugmentions((_B,_I))
rldot1qStaticUnicastEntry.setIndexNames(*dot1qStaticUnicastEntry.getIndexNames())
dot1qTpFdbEntry.registerAugmentions((_B,_J))
rldot1qTpFdbEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())
mibBuilder.exportSymbols(_B,**{'rlq-bridge-mib':rlq_bridge_mib,'rldot1q':rldot1q,'rldot1qStaticUnicastTable':rldot1qStaticUnicastTable,_I:rldot1qStaticUnicastEntry,'rldot1qStaticUnicastAddressOwner':rldot1qStaticUnicastAddressOwner,'rldot1qTpFdbTable':rldot1qTpFdbTable,_J:rldot1qTpFdbEntry,'rldot1qTpFdbSubStatus':rldot1qTpFdbSubStatus,'rldot1qTpFdbCountTable':rldot1qTpFdbCountTable,'rldot1qTpFdbCountEntry':rldot1qTpFdbCountEntry,_F:rldot1qTpFdbCountVlanTag,_G:rldot1qTpFdbCountPort,_H:rldot1qTpFdbCountType,'rldot1qTpFdbCountCount':rldot1qTpFdbCountCount})