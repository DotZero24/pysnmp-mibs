_H='colubrisSensorStatusMIBGroup'
_G='coSensorOperMode'
_F='coSensorConfigMode'
_E='coSensorOperState'
_D='read-only'
_C='Integer32'
_B='COLUBRIS-SENSOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisSensorMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,31))
_ColubrisSensorMIBObjects_ObjectIdentity=ObjectIdentity
colubrisSensorMIBObjects=_ColubrisSensorMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,31,1))
_CoSensorStatusGroup_ObjectIdentity=ObjectIdentity
coSensorStatusGroup=_CoSensorStatusGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,31,1,1))
class _CoSensorOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CoSensorOperState_Type.__name__=_C
_CoSensorOperState_Object=MibScalar
coSensorOperState=_CoSensorOperState_Object((1,3,6,1,4,1,8744,5,31,1,1,1),_CoSensorOperState_Type())
coSensorOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:coSensorOperState.setStatus(_A)
class _CoSensorConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('shared',1),('dedicated',2)))
_CoSensorConfigMode_Type.__name__=_C
_CoSensorConfigMode_Object=MibScalar
coSensorConfigMode=_CoSensorConfigMode_Object((1,3,6,1,4,1,8744,5,31,1,1,2),_CoSensorConfigMode_Type())
coSensorConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:coSensorConfigMode.setStatus(_A)
class _CoSensorOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('unknown',1),('workingNormally',2),('troubleshootingBG',3),('intrusionPreventionBG',4),('troubleshootingA',5),('troubleshootingABG',6),('troubleshootingAIntrusionPreventionBG',7),('intrusionPreventionA',8),('intrusionPreventionATroubleshootingBG',9),('intrusionPreventionABG',10),('upgradingSoftware',11),('noEthernetLink',12),('noIpAddress',13),('noRfManagerServer',14),('notActiveOrStarting',15)))
_CoSensorOperMode_Type.__name__=_C
_CoSensorOperMode_Object=MibScalar
coSensorOperMode=_CoSensorOperMode_Object((1,3,6,1,4,1,8744,5,31,1,1,3),_CoSensorOperMode_Type())
coSensorOperMode.setMaxAccess(_D)
if mibBuilder.loadTexts:coSensorOperMode.setStatus(_A)
_ColubrisSensorMIBConformance_ObjectIdentity=ObjectIdentity
colubrisSensorMIBConformance=_ColubrisSensorMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,31,2))
_ColubrisSensorMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisSensorMIBCompliances=_ColubrisSensorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,31,2,1))
_ColubrisSensorMIBGroups_ObjectIdentity=ObjectIdentity
colubrisSensorMIBGroups=_ColubrisSensorMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,31,2,2))
colubrisSensorStatusMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,31,2,2,1))
colubrisSensorStatusMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:colubrisSensorStatusMIBGroup.setStatus(_A)
colubrisSensorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,31,2,1,1))
colubrisSensorMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:colubrisSensorMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisSensorMIB':colubrisSensorMIB,'colubrisSensorMIBObjects':colubrisSensorMIBObjects,'coSensorStatusGroup':coSensorStatusGroup,_E:coSensorOperState,_F:coSensorConfigMode,_G:coSensorOperMode,'colubrisSensorMIBConformance':colubrisSensorMIBConformance,'colubrisSensorMIBCompliances':colubrisSensorMIBCompliances,'colubrisSensorMIBCompliance':colubrisSensorMIBCompliance,'colubrisSensorMIBGroups':colubrisSensorMIBGroups,_H:colubrisSensorStatusMIBGroup})