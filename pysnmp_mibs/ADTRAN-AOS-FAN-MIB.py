_J='adGenAOSFanNotificationGroup'
_I='adGenAOSFanTrapGroup'
_H='adGenAOSFanTrapCfgGroup'
_G='adGenAOSFanFailureResume'
_F='adGenAOSFanFailure'
_E='adGenAOSFanTrapEnable'
_D='Integer32'
_C='adGenAOSFanNumber'
_B='current'
_A='ADTRAN-AOS-FAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSCommon,adGenAOSConformance=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSCommon','adGenAOSConformance')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAOSFanMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,1,8))
if mibBuilder.loadTexts:adGenAOSFanMib.setRevisions(('2017-12-27 00:00','2013-10-22 00:00'))
_AdGenAOSFan_ObjectIdentity=ObjectIdentity
adGenAOSFan=_AdGenAOSFan_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,8))
_AdGenAOSFanTrap_ObjectIdentity=ObjectIdentity
adGenAOSFanTrap=_AdGenAOSFanTrap_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,8,0))
_AdGenAOSFanTrapControl_ObjectIdentity=ObjectIdentity
adGenAOSFanTrapControl=_AdGenAOSFanTrapControl_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,8,1))
class _AdGenAOSFanTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AdGenAOSFanTrapEnable_Type.__name__=_D
_AdGenAOSFanTrapEnable_Object=MibScalar
adGenAOSFanTrapEnable=_AdGenAOSFanTrapEnable_Object((1,3,6,1,4,1,664,5,53,1,8,1,1),_AdGenAOSFanTrapEnable_Type())
adGenAOSFanTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:adGenAOSFanTrapEnable.setStatus(_B)
_AdGenAOSFanInfo_ObjectIdentity=ObjectIdentity
adGenAOSFanInfo=_AdGenAOSFanInfo_ObjectIdentity((1,3,6,1,4,1,664,5,53,1,8,2))
_AdGenAOSFanNumber_Type=Integer32
_AdGenAOSFanNumber_Object=MibScalar
adGenAOSFanNumber=_AdGenAOSFanNumber_Object((1,3,6,1,4,1,664,5,53,1,8,2,1),_AdGenAOSFanNumber_Type())
adGenAOSFanNumber.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:adGenAOSFanNumber.setStatus(_B)
_AdGenAOSFanConformance_ObjectIdentity=ObjectIdentity
adGenAOSFanConformance=_AdGenAOSFanConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,17))
_AdGenAOSFanGroups_ObjectIdentity=ObjectIdentity
adGenAOSFanGroups=_AdGenAOSFanGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,17,1))
_AdGenAOSFanCompliances_ObjectIdentity=ObjectIdentity
adGenAOSFanCompliances=_AdGenAOSFanCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,17,2))
adGenAOSFanTrapCfgGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,17,1,1))
adGenAOSFanTrapCfgGroup.setObjects((_A,_E))
if mibBuilder.loadTexts:adGenAOSFanTrapCfgGroup.setStatus(_B)
adGenAOSFanTrapGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,17,1,2))
adGenAOSFanTrapGroup.setObjects((_A,_C))
if mibBuilder.loadTexts:adGenAOSFanTrapGroup.setStatus(_B)
adGenAOSFanFailure=NotificationType((1,3,6,1,4,1,664,5,53,1,8,0,1))
adGenAOSFanFailure.setObjects((_A,_C))
if mibBuilder.loadTexts:adGenAOSFanFailure.setStatus(_B)
adGenAOSFanFailureResume=NotificationType((1,3,6,1,4,1,664,5,53,1,8,0,2))
adGenAOSFanFailureResume.setObjects((_A,_C))
if mibBuilder.loadTexts:adGenAOSFanFailureResume.setStatus(_B)
adGenAOSFanNotificationGroup=NotificationGroup((1,3,6,1,4,1,664,5,53,99,17,1,3))
adGenAOSFanNotificationGroup.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:adGenAOSFanNotificationGroup.setStatus(_B)
adGenAOSFanFullCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,17,2,1))
adGenAOSFanFullCompliance.setObjects(*((_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:adGenAOSFanFullCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'adGenAOSFan':adGenAOSFan,'adGenAOSFanTrap':adGenAOSFanTrap,_F:adGenAOSFanFailure,_G:adGenAOSFanFailureResume,'adGenAOSFanTrapControl':adGenAOSFanTrapControl,_E:adGenAOSFanTrapEnable,'adGenAOSFanInfo':adGenAOSFanInfo,_C:adGenAOSFanNumber,'adGenAOSFanConformance':adGenAOSFanConformance,'adGenAOSFanGroups':adGenAOSFanGroups,_H:adGenAOSFanTrapCfgGroup,_I:adGenAOSFanTrapGroup,_J:adGenAOSFanNotificationGroup,'adGenAOSFanCompliances':adGenAOSFanCompliances,'adGenAOSFanFullCompliance':adGenAOSFanFullCompliance,'adGenAOSFanMib':adGenAOSFanMib})