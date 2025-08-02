_Q='qtechArpMIBGroup'
_P='qtechArpCurrentUnresolveNumber'
_O='qtechArpCurrentTotalNumber'
_N='qtechArpIfCacheTimeOut'
_M='qtechArpStatus'
_L='qtechArpEntryType'
_K='qtechArpType'
_J='qtechArpRemainAge'
_I='qtechArpPhysAddress'
_H='qtechArpIfIfIndex'
_G='read-create'
_F='qtechArpNetAddress'
_E='qtechArpIfIndex'
_D='Integer32'
_C='read-only'
_B='QTECH-ARP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
qtechArpMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,2))
if mibBuilder.loadTexts:qtechArpMIB.setRevisions(('2002-03-20 00:00',))
_QtechArpMIBObjects_ObjectIdentity=ObjectIdentity
qtechArpMIBObjects=_QtechArpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,2,1))
_QtechArpTable_Object=MibTable
qtechArpTable=_QtechArpTable_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,1))
if mibBuilder.loadTexts:qtechArpTable.setStatus(_A)
_QtechArpEntry_Object=MibTableRow
qtechArpEntry=_QtechArpEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,1,1))
qtechArpEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:qtechArpEntry.setStatus(_A)
_QtechArpIfIndex_Type=IfIndex
_QtechArpIfIndex_Object=MibTableColumn
qtechArpIfIndex=_QtechArpIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,1,1,1),_QtechArpIfIndex_Type())
qtechArpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechArpIfIndex.setStatus(_A)
_QtechArpPhysAddress_Type=PhysAddress
_QtechArpPhysAddress_Object=MibTableColumn
qtechArpPhysAddress=_QtechArpPhysAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,1,1,2),_QtechArpPhysAddress_Type())
qtechArpPhysAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechArpPhysAddress.setStatus(_A)
_QtechArpNetAddress_Type=IpAddress
_QtechArpNetAddress_Object=MibTableColumn
qtechArpNetAddress=_QtechArpNetAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,1,1,3),_QtechArpNetAddress_Type())
qtechArpNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechArpNetAddress.setStatus(_A)
_QtechArpRemainAge_Type=Integer32
_QtechArpRemainAge_Object=MibTableColumn
qtechArpRemainAge=_QtechArpRemainAge_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,1,1,4),_QtechArpRemainAge_Type())
qtechArpRemainAge.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechArpRemainAge.setStatus(_A)
class _QtechArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('arpa',1))
_QtechArpType_Type.__name__=_D
_QtechArpType_Object=MibTableColumn
qtechArpType=_QtechArpType_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,1,1,5),_QtechArpType_Type())
qtechArpType.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechArpType.setStatus(_A)
class _QtechArpEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('dynamic',2),('interface',3),('vrrp',4),('trusted',5)))
_QtechArpEntryType_Type.__name__=_D
_QtechArpEntryType_Object=MibTableColumn
qtechArpEntryType=_QtechArpEntryType_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,1,1,6),_QtechArpEntryType_Type())
qtechArpEntryType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechArpEntryType.setStatus(_A)
_QtechArpStatus_Type=RowStatus
_QtechArpStatus_Object=MibTableColumn
qtechArpStatus=_QtechArpStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,1,1,7),_QtechArpStatus_Type())
qtechArpStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechArpStatus.setStatus(_A)
_QtechArpIfTable_Object=MibTable
qtechArpIfTable=_QtechArpIfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,2))
if mibBuilder.loadTexts:qtechArpIfTable.setStatus(_A)
_QtechArpIfEntry_Object=MibTableRow
qtechArpIfEntry=_QtechArpIfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,2,1))
qtechArpIfEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechArpIfEntry.setStatus(_A)
_QtechArpIfIfIndex_Type=IfIndex
_QtechArpIfIfIndex_Object=MibTableColumn
qtechArpIfIfIndex=_QtechArpIfIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,2,1,1),_QtechArpIfIfIndex_Type())
qtechArpIfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechArpIfIfIndex.setStatus(_A)
class _QtechArpIfCacheTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,18000))
_QtechArpIfCacheTimeOut_Type.__name__=_D
_QtechArpIfCacheTimeOut_Object=MibTableColumn
qtechArpIfCacheTimeOut=_QtechArpIfCacheTimeOut_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,2,1,2),_QtechArpIfCacheTimeOut_Type())
qtechArpIfCacheTimeOut.setMaxAccess('read-write')
if mibBuilder.loadTexts:qtechArpIfCacheTimeOut.setStatus(_A)
_QtechArpCurrentTotalNumber_Type=Counter32
_QtechArpCurrentTotalNumber_Object=MibScalar
qtechArpCurrentTotalNumber=_QtechArpCurrentTotalNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,3),_QtechArpCurrentTotalNumber_Type())
qtechArpCurrentTotalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechArpCurrentTotalNumber.setStatus(_A)
_QtechArpCurrentUnresolveNumber_Type=Counter32
_QtechArpCurrentUnresolveNumber_Object=MibScalar
qtechArpCurrentUnresolveNumber=_QtechArpCurrentUnresolveNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,2,1,4),_QtechArpCurrentUnresolveNumber_Type())
qtechArpCurrentUnresolveNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechArpCurrentUnresolveNumber.setStatus(_A)
_QtechArpMIBConformance_ObjectIdentity=ObjectIdentity
qtechArpMIBConformance=_QtechArpMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,2,2))
_QtechArpMIBCompliances_ObjectIdentity=ObjectIdentity
qtechArpMIBCompliances=_QtechArpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,2,2,1))
_QtechArpMIBGroups_ObjectIdentity=ObjectIdentity
qtechArpMIBGroups=_QtechArpMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,2,2,2))
qtechArpMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,2,2,2,1))
qtechArpMIBGroup.setObjects(*((_B,_E),(_B,_I),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_H),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:qtechArpMIBGroup.setStatus(_A)
qtechArpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,2,2,1,1))
qtechArpMIBCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:qtechArpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechArpMIB':qtechArpMIB,'qtechArpMIBObjects':qtechArpMIBObjects,'qtechArpTable':qtechArpTable,'qtechArpEntry':qtechArpEntry,_E:qtechArpIfIndex,_I:qtechArpPhysAddress,_F:qtechArpNetAddress,_J:qtechArpRemainAge,_K:qtechArpType,_L:qtechArpEntryType,_M:qtechArpStatus,'qtechArpIfTable':qtechArpIfTable,'qtechArpIfEntry':qtechArpIfEntry,_H:qtechArpIfIfIndex,_N:qtechArpIfCacheTimeOut,_O:qtechArpCurrentTotalNumber,_P:qtechArpCurrentUnresolveNumber,'qtechArpMIBConformance':qtechArpMIBConformance,'qtechArpMIBCompliances':qtechArpMIBCompliances,'qtechArpMIBCompliance':qtechArpMIBCompliance,'qtechArpMIBGroups':qtechArpMIBGroups,_Q:qtechArpMIBGroup})