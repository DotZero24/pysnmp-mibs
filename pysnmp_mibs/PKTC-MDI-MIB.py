_P='pktcMdiGroup'
_O='pktcMdiNslRowStatus'
_N='pktcMdiNslPortListOut'
_M='pktcMdiNslPortListIn'
_L='pktcMdiNslName'
_K='pktcMdiMdiActivityStatus'
_J='pktcMdiMdiName'
_I='pktcMdiMdiType'
_H='pktcMdiNslIndex'
_G='read-only'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-create'
_B='PKTC-MDI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pktcApplicationMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','pktcApplicationMibs')
ifIndex,=mibBuilder.importSymbols(_D,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
pktcMdiMib=ModuleIdentity((1,3,6,1,4,1,4491,2,2,8,6))
if mibBuilder.loadTexts:pktcMdiMib.setRevisions(('2009-09-17 00:00','2009-02-26 00:00'))
class PktcMdiType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pots',1),('dectPP',2)))
_PktcMdiNotifications_ObjectIdentity=ObjectIdentity
pktcMdiNotifications=_PktcMdiNotifications_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,6,0))
_PktcMdiObjects_ObjectIdentity=ObjectIdentity
pktcMdiObjects=_PktcMdiObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,6,1))
_PktcMdiMdiTable_Object=MibTable
pktcMdiMdiTable=_PktcMdiMdiTable_Object((1,3,6,1,4,1,4491,2,2,8,6,1,1))
if mibBuilder.loadTexts:pktcMdiMdiTable.setStatus(_A)
_PktcMdiMdiEntry_Object=MibTableRow
pktcMdiMdiEntry=_PktcMdiMdiEntry_Object((1,3,6,1,4,1,4491,2,2,8,6,1,1,1))
pktcMdiMdiEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pktcMdiMdiEntry.setStatus(_A)
_PktcMdiMdiType_Type=PktcMdiType
_PktcMdiMdiType_Object=MibTableColumn
pktcMdiMdiType=_PktcMdiMdiType_Object((1,3,6,1,4,1,4491,2,2,8,6,1,1,1,1),_PktcMdiMdiType_Type())
pktcMdiMdiType.setMaxAccess(_G)
if mibBuilder.loadTexts:pktcMdiMdiType.setStatus(_A)
_PktcMdiMdiName_Type=SnmpAdminString
_PktcMdiMdiName_Object=MibTableColumn
pktcMdiMdiName=_PktcMdiMdiName_Object((1,3,6,1,4,1,4491,2,2,8,6,1,1,1,2),_PktcMdiMdiName_Type())
pktcMdiMdiName.setMaxAccess('read-write')
if mibBuilder.loadTexts:pktcMdiMdiName.setStatus(_A)
class _PktcMdiMdiActivityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_PktcMdiMdiActivityStatus_Type.__name__=_F
_PktcMdiMdiActivityStatus_Object=MibTableColumn
pktcMdiMdiActivityStatus=_PktcMdiMdiActivityStatus_Object((1,3,6,1,4,1,4491,2,2,8,6,1,1,1,3),_PktcMdiMdiActivityStatus_Type())
pktcMdiMdiActivityStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:pktcMdiMdiActivityStatus.setStatus(_A)
_PktcMdiNslTable_Object=MibTable
pktcMdiNslTable=_PktcMdiNslTable_Object((1,3,6,1,4,1,4491,2,2,8,6,1,2))
if mibBuilder.loadTexts:pktcMdiNslTable.setStatus(_A)
_PktcMdiNslEntry_Object=MibTableRow
pktcMdiNslEntry=_PktcMdiNslEntry_Object((1,3,6,1,4,1,4491,2,2,8,6,1,2,1))
pktcMdiNslEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:pktcMdiNslEntry.setStatus(_A)
_PktcMdiNslIndex_Type=Unsigned32
_PktcMdiNslIndex_Object=MibTableColumn
pktcMdiNslIndex=_PktcMdiNslIndex_Object((1,3,6,1,4,1,4491,2,2,8,6,1,2,1,1),_PktcMdiNslIndex_Type())
pktcMdiNslIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:pktcMdiNslIndex.setStatus(_A)
_PktcMdiNslName_Type=SnmpAdminString
_PktcMdiNslName_Object=MibTableColumn
pktcMdiNslName=_PktcMdiNslName_Object((1,3,6,1,4,1,4491,2,2,8,6,1,2,1,2),_PktcMdiNslName_Type())
pktcMdiNslName.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMdiNslName.setStatus(_A)
_PktcMdiNslPortListIn_Type=SnmpAdminString
_PktcMdiNslPortListIn_Object=MibTableColumn
pktcMdiNslPortListIn=_PktcMdiNslPortListIn_Object((1,3,6,1,4,1,4491,2,2,8,6,1,2,1,3),_PktcMdiNslPortListIn_Type())
pktcMdiNslPortListIn.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMdiNslPortListIn.setStatus(_A)
_PktcMdiNslPortListOut_Type=SnmpAdminString
_PktcMdiNslPortListOut_Object=MibTableColumn
pktcMdiNslPortListOut=_PktcMdiNslPortListOut_Object((1,3,6,1,4,1,4491,2,2,8,6,1,2,1,4),_PktcMdiNslPortListOut_Type())
pktcMdiNslPortListOut.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMdiNslPortListOut.setStatus(_A)
_PktcMdiNslRowStatus_Type=RowStatus
_PktcMdiNslRowStatus_Object=MibTableColumn
pktcMdiNslRowStatus=_PktcMdiNslRowStatus_Object((1,3,6,1,4,1,4491,2,2,8,6,1,2,1,5),_PktcMdiNslRowStatus_Type())
pktcMdiNslRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pktcMdiNslRowStatus.setStatus(_A)
_PktcMdiMibConformance_ObjectIdentity=ObjectIdentity
pktcMdiMibConformance=_PktcMdiMibConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,6,2))
_PktcMdiMibCompliances_ObjectIdentity=ObjectIdentity
pktcMdiMibCompliances=_PktcMdiMibCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,6,2,1))
_PktcMdiMibGroups_ObjectIdentity=ObjectIdentity
pktcMdiMibGroups=_PktcMdiMibGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,8,6,2,2))
pktcMdiGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,8,6,2,2,1))
pktcMdiGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:pktcMdiGroup.setStatus(_A)
pktcMdiCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,8,6,2,1,1))
pktcMdiCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:pktcMdiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PktcMdiType':PktcMdiType,'pktcMdiMib':pktcMdiMib,'pktcMdiNotifications':pktcMdiNotifications,'pktcMdiObjects':pktcMdiObjects,'pktcMdiMdiTable':pktcMdiMdiTable,'pktcMdiMdiEntry':pktcMdiMdiEntry,_I:pktcMdiMdiType,_J:pktcMdiMdiName,_K:pktcMdiMdiActivityStatus,'pktcMdiNslTable':pktcMdiNslTable,'pktcMdiNslEntry':pktcMdiNslEntry,_H:pktcMdiNslIndex,_L:pktcMdiNslName,_M:pktcMdiNslPortListIn,_N:pktcMdiNslPortListOut,_O:pktcMdiNslRowStatus,'pktcMdiMibConformance':pktcMdiMibConformance,'pktcMdiMibCompliances':pktcMdiMibCompliances,'pktcMdiCompliance':pktcMdiCompliance,'pktcMdiMibGroups':pktcMdiMibGroups,_P:pktcMdiGroup})