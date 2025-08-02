_G='ciscoL2L3IfConfigMIBGroup'
_F='cL2L3IfModeOper'
_E='cL2L3IfModeAdmin'
_D='ifIndex'
_C='IF-MIB'
_B='CISCO-L2L3-INTERFACE-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoL2L3IfConfigMIB=ModuleIdentity((1,3,6,1,4,1,9,9,151))
if mibBuilder.loadTexts:ciscoL2L3IfConfigMIB.setRevisions(('2000-05-10 19:00',))
class CL2L3InterfaceMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('routed',1),('switchport',2)))
_CiscoL2L3IfConfigMIBObjects_ObjectIdentity=ObjectIdentity
ciscoL2L3IfConfigMIBObjects=_CiscoL2L3IfConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,151,1))
_CL2L3IfConfig_ObjectIdentity=ObjectIdentity
cL2L3IfConfig=_CL2L3IfConfig_ObjectIdentity((1,3,6,1,4,1,9,9,151,1,1))
_CL2L3IfTable_Object=MibTable
cL2L3IfTable=_CL2L3IfTable_Object((1,3,6,1,4,1,9,9,151,1,1,1))
if mibBuilder.loadTexts:cL2L3IfTable.setStatus(_A)
_CL2L3IfEntry_Object=MibTableRow
cL2L3IfEntry=_CL2L3IfEntry_Object((1,3,6,1,4,1,9,9,151,1,1,1,1))
cL2L3IfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cL2L3IfEntry.setStatus(_A)
_CL2L3IfModeAdmin_Type=CL2L3InterfaceMode
_CL2L3IfModeAdmin_Object=MibTableColumn
cL2L3IfModeAdmin=_CL2L3IfModeAdmin_Object((1,3,6,1,4,1,9,9,151,1,1,1,1,1),_CL2L3IfModeAdmin_Type())
cL2L3IfModeAdmin.setMaxAccess('read-write')
if mibBuilder.loadTexts:cL2L3IfModeAdmin.setStatus(_A)
_CL2L3IfModeOper_Type=CL2L3InterfaceMode
_CL2L3IfModeOper_Object=MibTableColumn
cL2L3IfModeOper=_CL2L3IfModeOper_Object((1,3,6,1,4,1,9,9,151,1,1,1,1,2),_CL2L3IfModeOper_Type())
cL2L3IfModeOper.setMaxAccess('read-only')
if mibBuilder.loadTexts:cL2L3IfModeOper.setStatus(_A)
_CiscoL2L3IfConfigMIBConformance_ObjectIdentity=ObjectIdentity
ciscoL2L3IfConfigMIBConformance=_CiscoL2L3IfConfigMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,151,3))
_CiscoL2L3IfConfigMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoL2L3IfConfigMIBCompliances=_CiscoL2L3IfConfigMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,151,3,1))
_CiscoL2L3IfConfigMIBGroups_ObjectIdentity=ObjectIdentity
ciscoL2L3IfConfigMIBGroups=_CiscoL2L3IfConfigMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,151,3,2))
ciscoL2L3IfConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,151,3,2,1))
ciscoL2L3IfConfigMIBGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:ciscoL2L3IfConfigMIBGroup.setStatus(_A)
ciscoL2L3IfConfigMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,151,3,1,1))
ciscoL2L3IfConfigMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:ciscoL2L3IfConfigMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CL2L3InterfaceMode':CL2L3InterfaceMode,'ciscoL2L3IfConfigMIB':ciscoL2L3IfConfigMIB,'ciscoL2L3IfConfigMIBObjects':ciscoL2L3IfConfigMIBObjects,'cL2L3IfConfig':cL2L3IfConfig,'cL2L3IfTable':cL2L3IfTable,'cL2L3IfEntry':cL2L3IfEntry,_E:cL2L3IfModeAdmin,_F:cL2L3IfModeOper,'ciscoL2L3IfConfigMIBConformance':ciscoL2L3IfConfigMIBConformance,'ciscoL2L3IfConfigMIBCompliances':ciscoL2L3IfConfigMIBCompliances,'ciscoL2L3IfConfigMIBCompliance':ciscoL2L3IfConfigMIBCompliance,'ciscoL2L3IfConfigMIBGroups':ciscoL2L3IfConfigMIBGroups,_G:ciscoL2L3IfConfigMIBGroup})