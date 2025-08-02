_M='cggsnGeoPassiveGroup'
_L='cggsnGeoRowStatus'
_K='cggsnGeoVRFEnabled'
_J='cggsnGeoPassiveIfOnStdby'
_I='cggsnGeoPassiveStdbyIfName'
_H='cggsnGeoProcessNumber'
_G='Unsigned32'
_F='SnmpAdminString'
_E='ifIndex'
_D='IF-MIB'
_C='read-create'
_B='CISCO-GGSN-GEO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cggsnGeoMIB=ModuleIdentity((1,3,6,1,4,1,9,9,724))
if mibBuilder.loadTexts:cggsnGeoMIB.setRevisions(('2010-02-19 00:00',))
_CggsnGeoPassiveTable_Object=MibTable
cggsnGeoPassiveTable=_CggsnGeoPassiveTable_Object((1,3,6,1,4,1,9,9,724,1))
if mibBuilder.loadTexts:cggsnGeoPassiveTable.setStatus(_A)
_CggsnGeoPassiveEntry_Object=MibTableRow
cggsnGeoPassiveEntry=_CggsnGeoPassiveEntry_Object((1,3,6,1,4,1,9,9,724,1,1))
cggsnGeoPassiveEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:cggsnGeoPassiveEntry.setStatus(_A)
class _CggsnGeoProcessNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CggsnGeoProcessNumber_Type.__name__=_G
_CggsnGeoProcessNumber_Object=MibTableColumn
cggsnGeoProcessNumber=_CggsnGeoProcessNumber_Object((1,3,6,1,4,1,9,9,724,1,1,1),_CggsnGeoProcessNumber_Type())
cggsnGeoProcessNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cggsnGeoProcessNumber.setStatus(_A)
class _CggsnGeoPassiveStdbyIfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CggsnGeoPassiveStdbyIfName_Type.__name__=_F
_CggsnGeoPassiveStdbyIfName_Object=MibTableColumn
cggsnGeoPassiveStdbyIfName=_CggsnGeoPassiveStdbyIfName_Object((1,3,6,1,4,1,9,9,724,1,1,2),_CggsnGeoPassiveStdbyIfName_Type())
cggsnGeoPassiveStdbyIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnGeoPassiveStdbyIfName.setStatus(_A)
_CggsnGeoPassiveIfOnStdby_Type=TruthValue
_CggsnGeoPassiveIfOnStdby_Object=MibTableColumn
cggsnGeoPassiveIfOnStdby=_CggsnGeoPassiveIfOnStdby_Object((1,3,6,1,4,1,9,9,724,1,1,3),_CggsnGeoPassiveIfOnStdby_Type())
cggsnGeoPassiveIfOnStdby.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnGeoPassiveIfOnStdby.setStatus(_A)
_CggsnGeoVRFEnabled_Type=TruthValue
_CggsnGeoVRFEnabled_Object=MibTableColumn
cggsnGeoVRFEnabled=_CggsnGeoVRFEnabled_Object((1,3,6,1,4,1,9,9,724,1,1,4),_CggsnGeoVRFEnabled_Type())
cggsnGeoVRFEnabled.setMaxAccess('read-only')
if mibBuilder.loadTexts:cggsnGeoVRFEnabled.setStatus(_A)
_CggsnGeoRowStatus_Type=RowStatus
_CggsnGeoRowStatus_Object=MibTableColumn
cggsnGeoRowStatus=_CggsnGeoRowStatus_Object((1,3,6,1,4,1,9,9,724,1,1,5),_CggsnGeoRowStatus_Type())
cggsnGeoRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnGeoRowStatus.setStatus(_A)
_CggsnGeoConformance_ObjectIdentity=ObjectIdentity
cggsnGeoConformance=_CggsnGeoConformance_ObjectIdentity((1,3,6,1,4,1,9,9,724,2))
_CggsnGeogroups_ObjectIdentity=ObjectIdentity
cggsnGeogroups=_CggsnGeogroups_ObjectIdentity((1,3,6,1,4,1,9,9,724,2,1))
_CggsnGeoCompliances_ObjectIdentity=ObjectIdentity
cggsnGeoCompliances=_CggsnGeoCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,724,2,2))
cggsnGeoPassiveGroup=ObjectGroup((1,3,6,1,4,1,9,9,724,2,1,1))
cggsnGeoPassiveGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cggsnGeoPassiveGroup.setStatus(_A)
cggsnGeoCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,724,2,2,1))
cggsnGeoCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:cggsnGeoCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cggsnGeoMIB':cggsnGeoMIB,'cggsnGeoPassiveTable':cggsnGeoPassiveTable,'cggsnGeoPassiveEntry':cggsnGeoPassiveEntry,_H:cggsnGeoProcessNumber,_I:cggsnGeoPassiveStdbyIfName,_J:cggsnGeoPassiveIfOnStdby,_K:cggsnGeoVRFEnabled,_L:cggsnGeoRowStatus,'cggsnGeoConformance':cggsnGeoConformance,'cggsnGeogroups':cggsnGeogroups,_M:cggsnGeoPassiveGroup,'cggsnGeoCompliances':cggsnGeoCompliances,'cggsnGeoCompliance':cggsnGeoCompliance})