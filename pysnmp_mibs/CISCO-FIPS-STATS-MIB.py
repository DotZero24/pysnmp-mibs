_E='ciscoFipsStatsMIBGroup'
_D='cfipsPostStatus'
_C='Integer32'
_B='CISCO-FIPS-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoFipsStatsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,999999))
if mibBuilder.loadTexts:ciscoFipsStatsMIB.setRevisions(('2003-03-10 00:00',))
_CiscoFipsStatsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFipsStatsMIBNotifs=_CiscoFipsStatsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,999999,0))
_CiscoFipsStatsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFipsStatsMIBObjects=_CiscoFipsStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,999999,1))
_CfipsStats_ObjectIdentity=ObjectIdentity
cfipsStats=_CfipsStats_ObjectIdentity((1,3,6,1,4,1,9,9,999999,1,1))
_CfipsStatsGlobal_ObjectIdentity=ObjectIdentity
cfipsStatsGlobal=_CfipsStatsGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,999999,1,1,1))
class _CfipsPostStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('running',1),('passed',2),('failed',3),('notAvailable',4)))
_CfipsPostStatus_Type.__name__=_C
_CfipsPostStatus_Object=MibScalar
cfipsPostStatus=_CfipsPostStatus_Object((1,3,6,1,4,1,9,9,999999,1,1,1,1),_CfipsPostStatus_Type())
cfipsPostStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:cfipsPostStatus.setStatus(_A)
_CiscoFipsStatsMIBConform_ObjectIdentity=ObjectIdentity
ciscoFipsStatsMIBConform=_CiscoFipsStatsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,999999,2))
_CiscoFipsStatsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFipsStatsMIBCompliances=_CiscoFipsStatsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,999999,2,1))
_CiscoFipsStatsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFipsStatsMIBGroups=_CiscoFipsStatsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,999999,2,2))
ciscoFipsStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,999999,2,2,1))
ciscoFipsStatsMIBGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:ciscoFipsStatsMIBGroup.setStatus(_A)
ciscoFipsStatsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,999999,2,1,1))
ciscoFipsStatsMIBCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:ciscoFipsStatsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFipsStatsMIB':ciscoFipsStatsMIB,'ciscoFipsStatsMIBNotifs':ciscoFipsStatsMIBNotifs,'ciscoFipsStatsMIBObjects':ciscoFipsStatsMIBObjects,'cfipsStats':cfipsStats,'cfipsStatsGlobal':cfipsStatsGlobal,_D:cfipsPostStatus,'ciscoFipsStatsMIBConform':ciscoFipsStatsMIBConform,'ciscoFipsStatsMIBCompliances':ciscoFipsStatsMIBCompliances,'ciscoFipsStatsMIBCompliance':ciscoFipsStatsMIBCompliance,'ciscoFipsStatsMIBGroups':ciscoFipsStatsMIBGroups,_E:ciscoFipsStatsMIBGroup})