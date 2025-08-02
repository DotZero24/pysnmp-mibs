_Q='myArpMIBGroup'
_P='myArpCurrentUnresolveNumber'
_O='myArpCurrentTotalNumber'
_N='myArpIfCacheTimeOut'
_M='myArpStatus'
_L='myArpEntryType'
_K='myArpType'
_J='myArpRemainAge'
_I='myArpPhysAddress'
_H='myArpIfIfIndex'
_G='read-write'
_F='myArpNetAddress'
_E='myArpIfIndex'
_D='Integer32'
_C='read-only'
_B='MY-ARP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ip,=mibBuilder.importSymbols('IP-MIB','ip')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
IfIndex,=mibBuilder.importSymbols('MY-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
myArpMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,2))
if mibBuilder.loadTexts:myArpMIB.setRevisions(('2002-03-20 00:00',))
_MyArpMIBObjects_ObjectIdentity=ObjectIdentity
myArpMIBObjects=_MyArpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,2,1))
_MyArpTable_Object=MibTable
myArpTable=_MyArpTable_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,1))
if mibBuilder.loadTexts:myArpTable.setStatus(_A)
_MyArpEntry_Object=MibTableRow
myArpEntry=_MyArpEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,1,1))
myArpEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:myArpEntry.setStatus(_A)
_MyArpIfIndex_Type=IfIndex
_MyArpIfIndex_Object=MibTableColumn
myArpIfIndex=_MyArpIfIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,1,1,1),_MyArpIfIndex_Type())
myArpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myArpIfIndex.setStatus(_A)
_MyArpPhysAddress_Type=PhysAddress
_MyArpPhysAddress_Object=MibTableColumn
myArpPhysAddress=_MyArpPhysAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,1,1,2),_MyArpPhysAddress_Type())
myArpPhysAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:myArpPhysAddress.setStatus(_A)
_MyArpNetAddress_Type=IpAddress
_MyArpNetAddress_Object=MibTableColumn
myArpNetAddress=_MyArpNetAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,1,1,3),_MyArpNetAddress_Type())
myArpNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:myArpNetAddress.setStatus(_A)
_MyArpRemainAge_Type=Integer32
_MyArpRemainAge_Object=MibTableColumn
myArpRemainAge=_MyArpRemainAge_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,1,1,4),_MyArpRemainAge_Type())
myArpRemainAge.setMaxAccess(_C)
if mibBuilder.loadTexts:myArpRemainAge.setStatus(_A)
class _MyArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('arpa',1))
_MyArpType_Type.__name__=_D
_MyArpType_Object=MibTableColumn
myArpType=_MyArpType_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,1,1,5),_MyArpType_Type())
myArpType.setMaxAccess(_G)
if mibBuilder.loadTexts:myArpType.setStatus(_A)
class _MyArpEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('dynamic',2),('interface',3),('vrrp',4),('trusted',5)))
_MyArpEntryType_Type.__name__=_D
_MyArpEntryType_Object=MibTableColumn
myArpEntryType=_MyArpEntryType_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,1,1,6),_MyArpEntryType_Type())
myArpEntryType.setMaxAccess(_C)
if mibBuilder.loadTexts:myArpEntryType.setStatus(_A)
_MyArpStatus_Type=RowStatus
_MyArpStatus_Object=MibTableColumn
myArpStatus=_MyArpStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,1,1,7),_MyArpStatus_Type())
myArpStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:myArpStatus.setStatus(_A)
_MyArpIfTable_Object=MibTable
myArpIfTable=_MyArpIfTable_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,2))
if mibBuilder.loadTexts:myArpIfTable.setStatus(_A)
_MyArpIfEntry_Object=MibTableRow
myArpIfEntry=_MyArpIfEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,2,1))
myArpIfEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:myArpIfEntry.setStatus(_A)
_MyArpIfIfIndex_Type=IfIndex
_MyArpIfIfIndex_Object=MibTableColumn
myArpIfIfIndex=_MyArpIfIfIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,2,1,1),_MyArpIfIfIndex_Type())
myArpIfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myArpIfIfIndex.setStatus(_A)
class _MyArpIfCacheTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,18000))
_MyArpIfCacheTimeOut_Type.__name__=_D
_MyArpIfCacheTimeOut_Object=MibTableColumn
myArpIfCacheTimeOut=_MyArpIfCacheTimeOut_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,2,1,2),_MyArpIfCacheTimeOut_Type())
myArpIfCacheTimeOut.setMaxAccess(_G)
if mibBuilder.loadTexts:myArpIfCacheTimeOut.setStatus(_A)
_MyArpCurrentTotalNumber_Type=Counter32
_MyArpCurrentTotalNumber_Object=MibScalar
myArpCurrentTotalNumber=_MyArpCurrentTotalNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,3),_MyArpCurrentTotalNumber_Type())
myArpCurrentTotalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myArpCurrentTotalNumber.setStatus(_A)
_MyArpCurrentUnresolveNumber_Type=Counter32
_MyArpCurrentUnresolveNumber_Object=MibScalar
myArpCurrentUnresolveNumber=_MyArpCurrentUnresolveNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,2,1,4),_MyArpCurrentUnresolveNumber_Type())
myArpCurrentUnresolveNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myArpCurrentUnresolveNumber.setStatus(_A)
_MyArpMIBConformance_ObjectIdentity=ObjectIdentity
myArpMIBConformance=_MyArpMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,2,2))
_MyArpMIBCompliances_ObjectIdentity=ObjectIdentity
myArpMIBCompliances=_MyArpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,2,2,1))
_MyArpMIBGroups_ObjectIdentity=ObjectIdentity
myArpMIBGroups=_MyArpMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,2,2,2))
myArpMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,2,2,2,1))
myArpMIBGroup.setObjects(*((_B,_E),(_B,_I),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_H),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:myArpMIBGroup.setStatus(_A)
myArpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,2,2,1,1))
myArpMIBCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:myArpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myArpMIB':myArpMIB,'myArpMIBObjects':myArpMIBObjects,'myArpTable':myArpTable,'myArpEntry':myArpEntry,_E:myArpIfIndex,_I:myArpPhysAddress,_F:myArpNetAddress,_J:myArpRemainAge,_K:myArpType,_L:myArpEntryType,_M:myArpStatus,'myArpIfTable':myArpIfTable,'myArpIfEntry':myArpIfEntry,_H:myArpIfIfIndex,_N:myArpIfCacheTimeOut,_O:myArpCurrentTotalNumber,_P:myArpCurrentUnresolveNumber,'myArpMIBConformance':myArpMIBConformance,'myArpMIBCompliances':myArpMIBCompliances,'myArpMIBCompliance':myArpMIBCompliance,'myArpMIBGroups':myArpMIBGroups,_Q:myArpMIBGroup})