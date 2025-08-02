_N='cbpAcctTableGroupRev1'
_M='cbpAcctTableGroup'
_L='cbpAcctOutOctetCount'
_K='cbpAcctOutPacketCount'
_J='deprecated'
_I='Integer32'
_H='ifIndex'
_G='IF-MIB'
_F='cbpAcctInOctetCount'
_E='cbpAcctInPacketCount'
_D='cbpAcctTrafficIndex'
_C='read-only'
_B='current'
_A='CISCO-BGP-POLICY-ACCOUNTING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoBgpPolAcctMIB=ModuleIdentity((1,3,6,1,4,1,9,9,148))
if mibBuilder.loadTexts:ciscoBgpPolAcctMIB.setRevisions(('2002-07-26 00:00','1999-12-17 00:00'))
_CiscoBgpPolAcctMIBObjects_ObjectIdentity=ObjectIdentity
ciscoBgpPolAcctMIBObjects=_CiscoBgpPolAcctMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,148,1))
_CbpAcctTable_Object=MibTable
cbpAcctTable=_CbpAcctTable_Object((1,3,6,1,4,1,9,9,148,1,1))
if mibBuilder.loadTexts:cbpAcctTable.setStatus(_B)
_CbpAcctEntry_Object=MibTableRow
cbpAcctEntry=_CbpAcctEntry_Object((1,3,6,1,4,1,9,9,148,1,1,1))
cbpAcctEntry.setIndexNames((0,_G,_H),(0,_A,_D))
if mibBuilder.loadTexts:cbpAcctEntry.setStatus(_B)
class _CbpAcctTrafficIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CbpAcctTrafficIndex_Type.__name__=_I
_CbpAcctTrafficIndex_Object=MibTableColumn
cbpAcctTrafficIndex=_CbpAcctTrafficIndex_Object((1,3,6,1,4,1,9,9,148,1,1,1,1),_CbpAcctTrafficIndex_Type())
cbpAcctTrafficIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cbpAcctTrafficIndex.setStatus(_B)
_CbpAcctInPacketCount_Type=Counter64
_CbpAcctInPacketCount_Object=MibTableColumn
cbpAcctInPacketCount=_CbpAcctInPacketCount_Object((1,3,6,1,4,1,9,9,148,1,1,1,2),_CbpAcctInPacketCount_Type())
cbpAcctInPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cbpAcctInPacketCount.setStatus(_B)
_CbpAcctInOctetCount_Type=Counter64
_CbpAcctInOctetCount_Object=MibTableColumn
cbpAcctInOctetCount=_CbpAcctInOctetCount_Object((1,3,6,1,4,1,9,9,148,1,1,1,3),_CbpAcctInOctetCount_Type())
cbpAcctInOctetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cbpAcctInOctetCount.setStatus(_B)
_CbpAcctOutPacketCount_Type=Counter64
_CbpAcctOutPacketCount_Object=MibTableColumn
cbpAcctOutPacketCount=_CbpAcctOutPacketCount_Object((1,3,6,1,4,1,9,9,148,1,1,1,4),_CbpAcctOutPacketCount_Type())
cbpAcctOutPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cbpAcctOutPacketCount.setStatus(_B)
_CbpAcctOutOctetCount_Type=Counter64
_CbpAcctOutOctetCount_Object=MibTableColumn
cbpAcctOutOctetCount=_CbpAcctOutOctetCount_Object((1,3,6,1,4,1,9,9,148,1,1,1,5),_CbpAcctOutOctetCount_Type())
cbpAcctOutOctetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cbpAcctOutOctetCount.setStatus(_B)
_CiscoBgpPolAcctMIBConformance_ObjectIdentity=ObjectIdentity
ciscoBgpPolAcctMIBConformance=_CiscoBgpPolAcctMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,148,3))
_CiscoBgpPolAcctMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoBgpPolAcctMIBCompliances=_CiscoBgpPolAcctMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,148,3,1))
_CiscoBgpPolAcctMIBGroups_ObjectIdentity=ObjectIdentity
ciscoBgpPolAcctMIBGroups=_CiscoBgpPolAcctMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,148,3,2))
cbpAcctTableGroup=ObjectGroup((1,3,6,1,4,1,9,9,148,3,2,1))
cbpAcctTableGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:cbpAcctTableGroup.setStatus(_J)
cbpAcctTableGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,148,3,2,2))
cbpAcctTableGroupRev1.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cbpAcctTableGroupRev1.setStatus(_B)
ciscoBgpPolAcctMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,148,3,1,1))
ciscoBgpPolAcctMIBCompliance.setObjects((_A,_M))
if mibBuilder.loadTexts:ciscoBgpPolAcctMIBCompliance.setStatus(_J)
ciscoBgpPolAcctMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,148,3,1,2))
ciscoBgpPolAcctMIBComplianceRev1.setObjects((_A,_N))
if mibBuilder.loadTexts:ciscoBgpPolAcctMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoBgpPolAcctMIB':ciscoBgpPolAcctMIB,'ciscoBgpPolAcctMIBObjects':ciscoBgpPolAcctMIBObjects,'cbpAcctTable':cbpAcctTable,'cbpAcctEntry':cbpAcctEntry,_D:cbpAcctTrafficIndex,_E:cbpAcctInPacketCount,_F:cbpAcctInOctetCount,_K:cbpAcctOutPacketCount,_L:cbpAcctOutOctetCount,'ciscoBgpPolAcctMIBConformance':ciscoBgpPolAcctMIBConformance,'ciscoBgpPolAcctMIBCompliances':ciscoBgpPolAcctMIBCompliances,'ciscoBgpPolAcctMIBCompliance':ciscoBgpPolAcctMIBCompliance,'ciscoBgpPolAcctMIBComplianceRev1':ciscoBgpPolAcctMIBComplianceRev1,'ciscoBgpPolAcctMIBGroups':ciscoBgpPolAcctMIBGroups,_M:cbpAcctTableGroup,_N:cbpAcctTableGroupRev1})