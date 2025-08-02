_P='cPtopoExtCdpProxyGroup'
_O='cPtopoExtCdpGroup'
_N='cPtopoConnExtGroup'
_M='cPtopoExtCdpProxyIf'
_L='cPtopoExtCdpRowStatus'
_K='cPtopoExtCdpDiscoveryState'
_J='cPtopoConnExtLinkDirection'
_I='cPtopoConnExtEntry'
_H='not-accessible'
_G='cPtopoExtCdpLocalPort'
_F='cPtopoExtCdpLocalChassis'
_E='InterfaceIndexOrZero'
_D='read-create'
_C='Integer32'
_B='CISCO-PTOPO-EXTN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_E)
ptopoConnEntry,=mibBuilder.importSymbols('PTOPO-MIB','ptopoConnEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoPtopoExtnMIB=ModuleIdentity((1,3,6,1,4,1,9,9,261))
if mibBuilder.loadTexts:ciscoPtopoExtnMIB.setRevisions(('2002-05-12 00:00',))
_CiscoPtopoExtnMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPtopoExtnMIBObjects=_CiscoPtopoExtnMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,261,1))
_CPtopoConnExtTable_Object=MibTable
cPtopoConnExtTable=_CPtopoConnExtTable_Object((1,3,6,1,4,1,9,9,261,1,1))
if mibBuilder.loadTexts:cPtopoConnExtTable.setStatus(_A)
_CPtopoConnExtEntry_Object=MibTableRow
cPtopoConnExtEntry=_CPtopoConnExtEntry_Object((1,3,6,1,4,1,9,9,261,1,1,1))
if mibBuilder.loadTexts:cPtopoConnExtEntry.setStatus(_A)
class _CPtopoConnExtLinkDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transmit',1),('receive',2),('both',3)))
_CPtopoConnExtLinkDirection_Type.__name__=_C
_CPtopoConnExtLinkDirection_Object=MibTableColumn
cPtopoConnExtLinkDirection=_CPtopoConnExtLinkDirection_Object((1,3,6,1,4,1,9,9,261,1,1,1,1),_CPtopoConnExtLinkDirection_Type())
cPtopoConnExtLinkDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cPtopoConnExtLinkDirection.setStatus(_A)
_CPtopoExtCdpTable_Object=MibTable
cPtopoExtCdpTable=_CPtopoExtCdpTable_Object((1,3,6,1,4,1,9,9,261,1,2))
if mibBuilder.loadTexts:cPtopoExtCdpTable.setStatus(_A)
_CPtopoExtCdpEntry_Object=MibTableRow
cPtopoExtCdpEntry=_CPtopoExtCdpEntry_Object((1,3,6,1,4,1,9,9,261,1,2,1))
cPtopoExtCdpEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:cPtopoExtCdpEntry.setStatus(_A)
_CPtopoExtCdpLocalChassis_Type=PhysicalIndex
_CPtopoExtCdpLocalChassis_Object=MibTableColumn
cPtopoExtCdpLocalChassis=_CPtopoExtCdpLocalChassis_Object((1,3,6,1,4,1,9,9,261,1,2,1,1),_CPtopoExtCdpLocalChassis_Type())
cPtopoExtCdpLocalChassis.setMaxAccess(_H)
if mibBuilder.loadTexts:cPtopoExtCdpLocalChassis.setStatus(_A)
_CPtopoExtCdpLocalPort_Type=PhysicalIndex
_CPtopoExtCdpLocalPort_Object=MibTableColumn
cPtopoExtCdpLocalPort=_CPtopoExtCdpLocalPort_Object((1,3,6,1,4,1,9,9,261,1,2,1,2),_CPtopoExtCdpLocalPort_Type())
cPtopoExtCdpLocalPort.setMaxAccess(_H)
if mibBuilder.loadTexts:cPtopoExtCdpLocalPort.setStatus(_A)
class _CPtopoExtCdpDiscoveryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cdpDisabled',1),('interfaceDown',2),('waiting',3),('discovered',4)))
_CPtopoExtCdpDiscoveryState_Type.__name__=_C
_CPtopoExtCdpDiscoveryState_Object=MibTableColumn
cPtopoExtCdpDiscoveryState=_CPtopoExtCdpDiscoveryState_Object((1,3,6,1,4,1,9,9,261,1,2,1,3),_CPtopoExtCdpDiscoveryState_Type())
cPtopoExtCdpDiscoveryState.setMaxAccess('read-only')
if mibBuilder.loadTexts:cPtopoExtCdpDiscoveryState.setStatus(_A)
class _CPtopoExtCdpProxyIf_Type(InterfaceIndexOrZero):defaultValue=0
_CPtopoExtCdpProxyIf_Type.__name__=_E
_CPtopoExtCdpProxyIf_Object=MibTableColumn
cPtopoExtCdpProxyIf=_CPtopoExtCdpProxyIf_Object((1,3,6,1,4,1,9,9,261,1,2,1,4),_CPtopoExtCdpProxyIf_Type())
cPtopoExtCdpProxyIf.setMaxAccess(_D)
if mibBuilder.loadTexts:cPtopoExtCdpProxyIf.setStatus(_A)
_CPtopoExtCdpRowStatus_Type=RowStatus
_CPtopoExtCdpRowStatus_Object=MibTableColumn
cPtopoExtCdpRowStatus=_CPtopoExtCdpRowStatus_Object((1,3,6,1,4,1,9,9,261,1,2,1,5),_CPtopoExtCdpRowStatus_Type())
cPtopoExtCdpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cPtopoExtCdpRowStatus.setStatus(_A)
_CPtopoExtnConformance_ObjectIdentity=ObjectIdentity
cPtopoExtnConformance=_CPtopoExtnConformance_ObjectIdentity((1,3,6,1,4,1,9,9,261,3))
_CPtopoExtnCompliances_ObjectIdentity=ObjectIdentity
cPtopoExtnCompliances=_CPtopoExtnCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,261,3,1))
_CPtopoExtnGroups_ObjectIdentity=ObjectIdentity
cPtopoExtnGroups=_CPtopoExtnGroups_ObjectIdentity((1,3,6,1,4,1,9,9,261,3,2))
ptopoConnEntry.registerAugmentions((_B,_I))
cPtopoConnExtEntry.setIndexNames(*ptopoConnEntry.getIndexNames())
cPtopoConnExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,261,3,2,1))
cPtopoConnExtGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:cPtopoConnExtGroup.setStatus(_A)
cPtopoExtCdpGroup=ObjectGroup((1,3,6,1,4,1,9,9,261,3,2,2))
cPtopoExtCdpGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cPtopoExtCdpGroup.setStatus(_A)
cPtopoExtCdpProxyGroup=ObjectGroup((1,3,6,1,4,1,9,9,261,3,2,3))
cPtopoExtCdpProxyGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:cPtopoExtCdpProxyGroup.setStatus(_A)
cPtopoExtnCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,261,3,1,1))
cPtopoExtnCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cPtopoExtnCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoPtopoExtnMIB':ciscoPtopoExtnMIB,'ciscoPtopoExtnMIBObjects':ciscoPtopoExtnMIBObjects,'cPtopoConnExtTable':cPtopoConnExtTable,_I:cPtopoConnExtEntry,_J:cPtopoConnExtLinkDirection,'cPtopoExtCdpTable':cPtopoExtCdpTable,'cPtopoExtCdpEntry':cPtopoExtCdpEntry,_F:cPtopoExtCdpLocalChassis,_G:cPtopoExtCdpLocalPort,_K:cPtopoExtCdpDiscoveryState,_M:cPtopoExtCdpProxyIf,_L:cPtopoExtCdpRowStatus,'cPtopoExtnConformance':cPtopoExtnConformance,'cPtopoExtnCompliances':cPtopoExtnCompliances,'cPtopoExtnCompliance':cPtopoExtnCompliance,'cPtopoExtnGroups':cPtopoExtnGroups,_N:cPtopoConnExtGroup,_O:cPtopoExtCdpGroup,_P:cPtopoExtCdpProxyGroup})