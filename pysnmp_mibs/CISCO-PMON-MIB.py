_M='ciscoPmonPortGroupStatsGroup'
_L='ciscoPmonPortGroupStatsValue'
_K='ciscoPmonPortGroupIfIndexList'
_J='read-only'
_I='not-accessible'
_H='ciscoPmonPortGroupIndex'
_G='ciscoPmonPortGroupStatsType'
_F='Unsigned32'
_E='Integer32'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='CISCO-PMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoInterfaceIndexList,=mibBuilder.importSymbols('CISCO-TC','CiscoInterfaceIndexList')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoPmonMIB=ModuleIdentity((1,3,6,1,4,1,9,9,779))
if mibBuilder.loadTexts:ciscoPmonMIB.setRevisions(('2012-01-03 00:00',))
_CiscoPmonMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPmonMIBNotifs=_CiscoPmonMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,779,0))
_CiscoPmonMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPmonMIBObjects=_CiscoPmonMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,779,1))
_CiscoPmonStatsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPmonStatsMIBObjects=_CiscoPmonStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,779,1,1))
_CiscoPmonPortGroupStatsTable_Object=MibTable
ciscoPmonPortGroupStatsTable=_CiscoPmonPortGroupStatsTable_Object((1,3,6,1,4,1,9,9,779,1,1,1))
if mibBuilder.loadTexts:ciscoPmonPortGroupStatsTable.setStatus(_A)
_CiscoPmonPortGroupStatsEntry_Object=MibTableRow
ciscoPmonPortGroupStatsEntry=_CiscoPmonPortGroupStatsEntry_Object((1,3,6,1,4,1,9,9,779,1,1,1,1))
ciscoPmonPortGroupStatsEntry.setIndexNames((0,_C,_D),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:ciscoPmonPortGroupStatsEntry.setStatus(_A)
class _CiscoPmonPortGroupStatsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('errPktsFromPort',1),('errPktsToXbar',2),('errPktsFromXbar',3)))
_CiscoPmonPortGroupStatsType_Type.__name__=_E
_CiscoPmonPortGroupStatsType_Object=MibTableColumn
ciscoPmonPortGroupStatsType=_CiscoPmonPortGroupStatsType_Object((1,3,6,1,4,1,9,9,779,1,1,1,1,1),_CiscoPmonPortGroupStatsType_Type())
ciscoPmonPortGroupStatsType.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoPmonPortGroupStatsType.setStatus(_A)
class _CiscoPmonPortGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CiscoPmonPortGroupIndex_Type.__name__=_F
_CiscoPmonPortGroupIndex_Object=MibTableColumn
ciscoPmonPortGroupIndex=_CiscoPmonPortGroupIndex_Object((1,3,6,1,4,1,9,9,779,1,1,1,1,2),_CiscoPmonPortGroupIndex_Type())
ciscoPmonPortGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoPmonPortGroupIndex.setStatus(_A)
_CiscoPmonPortGroupIfIndexList_Type=CiscoInterfaceIndexList
_CiscoPmonPortGroupIfIndexList_Object=MibTableColumn
ciscoPmonPortGroupIfIndexList=_CiscoPmonPortGroupIfIndexList_Object((1,3,6,1,4,1,9,9,779,1,1,1,1,3),_CiscoPmonPortGroupIfIndexList_Type())
ciscoPmonPortGroupIfIndexList.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoPmonPortGroupIfIndexList.setStatus(_A)
_CiscoPmonPortGroupStatsValue_Type=Counter64
_CiscoPmonPortGroupStatsValue_Object=MibTableColumn
ciscoPmonPortGroupStatsValue=_CiscoPmonPortGroupStatsValue_Object((1,3,6,1,4,1,9,9,779,1,1,1,1,4),_CiscoPmonPortGroupStatsValue_Type())
ciscoPmonPortGroupStatsValue.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoPmonPortGroupStatsValue.setStatus(_A)
_CiscoPmonMIBConformance_ObjectIdentity=ObjectIdentity
ciscoPmonMIBConformance=_CiscoPmonMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,779,2))
_CiscoPmonMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPmonMIBCompliances=_CiscoPmonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,779,2,1))
_CiscoPmonMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPmonMIBGroups=_CiscoPmonMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,779,2,2))
ciscoPmonPortGroupStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,779,2,2,1))
ciscoPmonPortGroupStatsGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ciscoPmonPortGroupStatsGroup.setStatus(_A)
ciscoPmonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,779,2,1,1))
ciscoPmonMIBCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:ciscoPmonMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoPmonMIB':ciscoPmonMIB,'ciscoPmonMIBNotifs':ciscoPmonMIBNotifs,'ciscoPmonMIBObjects':ciscoPmonMIBObjects,'ciscoPmonStatsMIBObjects':ciscoPmonStatsMIBObjects,'ciscoPmonPortGroupStatsTable':ciscoPmonPortGroupStatsTable,'ciscoPmonPortGroupStatsEntry':ciscoPmonPortGroupStatsEntry,_G:ciscoPmonPortGroupStatsType,_H:ciscoPmonPortGroupIndex,_K:ciscoPmonPortGroupIfIndexList,_L:ciscoPmonPortGroupStatsValue,'ciscoPmonMIBConformance':ciscoPmonMIBConformance,'ciscoPmonMIBCompliances':ciscoPmonMIBCompliances,'ciscoPmonMIBCompliance':ciscoPmonMIBCompliance,'ciscoPmonMIBGroups':ciscoPmonMIBGroups,_M:ciscoPmonPortGroupStatsGroup})