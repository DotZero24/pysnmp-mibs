_G='mServStatusGroup'
_F='mServServiceStatus'
_E='read-only'
_D='Integer32'
_C='mServServiceName'
_B='MDS-SERVICES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mdsServices,=mibBuilder.importSymbols('MDS-ORBIT-SMI-MIB','mdsServices')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mdsServicesMIB=ModuleIdentity((1,3,6,1,4,1,4130,10,3,1))
if mibBuilder.loadTexts:mdsServicesMIB.setRevisions(('2018-05-16 00:00','2014-10-20 00:00','2014-05-12 00:00'))
_MServMIBObjects_ObjectIdentity=ObjectIdentity
mServMIBObjects=_MServMIBObjects_ObjectIdentity((1,3,6,1,4,1,4130,10,3,1,1))
_MServConfig_ObjectIdentity=ObjectIdentity
mServConfig=_MServConfig_ObjectIdentity((1,3,6,1,4,1,4130,10,3,1,1,1))
_MServStatus_ObjectIdentity=ObjectIdentity
mServStatus=_MServStatus_ObjectIdentity((1,3,6,1,4,1,4130,10,3,1,1,2))
_MServStatusTable_Object=MibTable
mServStatusTable=_MServStatusTable_Object((1,3,6,1,4,1,4130,10,3,1,1,2,1))
if mibBuilder.loadTexts:mServStatusTable.setStatus(_A)
_MServStatusEntry_Object=MibTableRow
mServStatusEntry=_MServStatusEntry_Object((1,3,6,1,4,1,4130,10,3,1,1,2,1,1))
mServStatusEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:mServStatusEntry.setStatus(_A)
_MServServiceName_Type=OctetString
_MServServiceName_Object=MibTableColumn
mServServiceName=_MServServiceName_Object((1,3,6,1,4,1,4130,10,3,1,1,2,1,1,1),_MServServiceName_Type())
mServServiceName.setMaxAccess(_E)
if mibBuilder.loadTexts:mServServiceName.setStatus(_A)
class _MServServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('running',0),('disabled',1),('error',2),('notRunning',3)))
_MServServiceStatus_Type.__name__=_D
_MServServiceStatus_Object=MibTableColumn
mServServiceStatus=_MServServiceStatus_Object((1,3,6,1,4,1,4130,10,3,1,1,2,1,1,2),_MServServiceStatus_Type())
mServServiceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mServServiceStatus.setStatus(_A)
_MdsServMIBConformance_ObjectIdentity=ObjectIdentity
mdsServMIBConformance=_MdsServMIBConformance_ObjectIdentity((1,3,6,1,4,1,4130,10,3,1,3))
_MdsServMIBCompliances_ObjectIdentity=ObjectIdentity
mdsServMIBCompliances=_MdsServMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4130,10,3,1,3,1))
_MdsServMIBGroups_ObjectIdentity=ObjectIdentity
mdsServMIBGroups=_MdsServMIBGroups_ObjectIdentity((1,3,6,1,4,1,4130,10,3,1,3,2))
mServStatusGroup=ObjectGroup((1,3,6,1,4,1,4130,10,3,1,3,2,1))
mServStatusGroup.setObjects(*((_B,_C),(_B,_F)))
if mibBuilder.loadTexts:mServStatusGroup.setStatus(_A)
mServCompliance=ModuleCompliance((1,3,6,1,4,1,4130,10,3,1,3,1,1))
mServCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:mServCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mdsServicesMIB':mdsServicesMIB,'mServMIBObjects':mServMIBObjects,'mServConfig':mServConfig,'mServStatus':mServStatus,'mServStatusTable':mServStatusTable,'mServStatusEntry':mServStatusEntry,_C:mServServiceName,_F:mServServiceStatus,'mdsServMIBConformance':mdsServMIBConformance,'mdsServMIBCompliances':mdsServMIBCompliances,'mServCompliance':mServCompliance,'mdsServMIBGroups':mdsServMIBGroups,_G:mServStatusGroup})