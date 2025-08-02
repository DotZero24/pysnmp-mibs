_Q='fsArpMIBGroup'
_P='fsArpCurrentUnresolveNumber'
_O='fsArpCurrentTotalNumber'
_N='fsArpIfCacheTimeOut'
_M='fsArpStatus'
_L='fsArpEntryType'
_K='fsArpType'
_J='fsArpRemainAge'
_I='fsArpPhysAddress'
_H='fsArpIfIfIndex'
_G='read-create'
_F='fsArpNetAddress'
_E='fsArpIfIndex'
_D='Integer32'
_C='read-only'
_B='FS-ARP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsArpMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,2))
if mibBuilder.loadTexts:fsArpMIB.setRevisions(('2002-03-20 00:00',))
_FsArpMIBObjects_ObjectIdentity=ObjectIdentity
fsArpMIBObjects=_FsArpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,2,1))
_FsArpTable_Object=MibTable
fsArpTable=_FsArpTable_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,1))
if mibBuilder.loadTexts:fsArpTable.setStatus(_A)
_FsArpEntry_Object=MibTableRow
fsArpEntry=_FsArpEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,1,1))
fsArpEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:fsArpEntry.setStatus(_A)
_FsArpIfIndex_Type=IfIndex
_FsArpIfIndex_Object=MibTableColumn
fsArpIfIndex=_FsArpIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,1,1,1),_FsArpIfIndex_Type())
fsArpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpIfIndex.setStatus(_A)
_FsArpPhysAddress_Type=PhysAddress
_FsArpPhysAddress_Object=MibTableColumn
fsArpPhysAddress=_FsArpPhysAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,1,1,2),_FsArpPhysAddress_Type())
fsArpPhysAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:fsArpPhysAddress.setStatus(_A)
_FsArpNetAddress_Type=IpAddress
_FsArpNetAddress_Object=MibTableColumn
fsArpNetAddress=_FsArpNetAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,1,1,3),_FsArpNetAddress_Type())
fsArpNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpNetAddress.setStatus(_A)
_FsArpRemainAge_Type=Integer32
_FsArpRemainAge_Object=MibTableColumn
fsArpRemainAge=_FsArpRemainAge_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,1,1,4),_FsArpRemainAge_Type())
fsArpRemainAge.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpRemainAge.setStatus(_A)
class _FsArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('arpa',1))
_FsArpType_Type.__name__=_D
_FsArpType_Object=MibTableColumn
fsArpType=_FsArpType_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,1,1,5),_FsArpType_Type())
fsArpType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsArpType.setStatus(_A)
class _FsArpEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('dynamic',2),('interface',3),('vrrp',4),('trusted',5)))
_FsArpEntryType_Type.__name__=_D
_FsArpEntryType_Object=MibTableColumn
fsArpEntryType=_FsArpEntryType_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,1,1,6),_FsArpEntryType_Type())
fsArpEntryType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpEntryType.setStatus(_A)
_FsArpStatus_Type=RowStatus
_FsArpStatus_Object=MibTableColumn
fsArpStatus=_FsArpStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,1,1,7),_FsArpStatus_Type())
fsArpStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsArpStatus.setStatus(_A)
_FsArpIfTable_Object=MibTable
fsArpIfTable=_FsArpIfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,2))
if mibBuilder.loadTexts:fsArpIfTable.setStatus(_A)
_FsArpIfEntry_Object=MibTableRow
fsArpIfEntry=_FsArpIfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,2,1))
fsArpIfEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:fsArpIfEntry.setStatus(_A)
_FsArpIfIfIndex_Type=IfIndex
_FsArpIfIfIndex_Object=MibTableColumn
fsArpIfIfIndex=_FsArpIfIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,2,1,1),_FsArpIfIfIndex_Type())
fsArpIfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpIfIfIndex.setStatus(_A)
class _FsArpIfCacheTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,18000))
_FsArpIfCacheTimeOut_Type.__name__=_D
_FsArpIfCacheTimeOut_Object=MibTableColumn
fsArpIfCacheTimeOut=_FsArpIfCacheTimeOut_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,2,1,2),_FsArpIfCacheTimeOut_Type())
fsArpIfCacheTimeOut.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsArpIfCacheTimeOut.setStatus(_A)
_FsArpCurrentTotalNumber_Type=Counter32
_FsArpCurrentTotalNumber_Object=MibScalar
fsArpCurrentTotalNumber=_FsArpCurrentTotalNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,3),_FsArpCurrentTotalNumber_Type())
fsArpCurrentTotalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpCurrentTotalNumber.setStatus(_A)
_FsArpCurrentUnresolveNumber_Type=Counter32
_FsArpCurrentUnresolveNumber_Object=MibScalar
fsArpCurrentUnresolveNumber=_FsArpCurrentUnresolveNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,2,1,4),_FsArpCurrentUnresolveNumber_Type())
fsArpCurrentUnresolveNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsArpCurrentUnresolveNumber.setStatus(_A)
_FsArpMIBConformance_ObjectIdentity=ObjectIdentity
fsArpMIBConformance=_FsArpMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,2,2))
_FsArpMIBCompliances_ObjectIdentity=ObjectIdentity
fsArpMIBCompliances=_FsArpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,2,2,1))
_FsArpMIBGroups_ObjectIdentity=ObjectIdentity
fsArpMIBGroups=_FsArpMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,2,2,2))
fsArpMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,2,2,2,1))
fsArpMIBGroup.setObjects(*((_B,_E),(_B,_I),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_H),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:fsArpMIBGroup.setStatus(_A)
fsArpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,2,2,1,1))
fsArpMIBCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:fsArpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsArpMIB':fsArpMIB,'fsArpMIBObjects':fsArpMIBObjects,'fsArpTable':fsArpTable,'fsArpEntry':fsArpEntry,_E:fsArpIfIndex,_I:fsArpPhysAddress,_F:fsArpNetAddress,_J:fsArpRemainAge,_K:fsArpType,_L:fsArpEntryType,_M:fsArpStatus,'fsArpIfTable':fsArpIfTable,'fsArpIfEntry':fsArpIfEntry,_H:fsArpIfIfIndex,_N:fsArpIfCacheTimeOut,_O:fsArpCurrentTotalNumber,_P:fsArpCurrentUnresolveNumber,'fsArpMIBConformance':fsArpMIBConformance,'fsArpMIBCompliances':fsArpMIBCompliances,'fsArpMIBCompliance':fsArpMIBCompliance,'fsArpMIBGroups':fsArpMIBGroups,_Q:fsArpMIBGroup})