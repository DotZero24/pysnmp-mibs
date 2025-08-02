_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ubntSunMax,ubntSunMaxGroups=mibBuilder.importSymbols('UBNT-MIB','ubntSunMax','ubntSunMaxGroups')
sunMaxMIB=ModuleIdentity((1,3,6,1,4,1,41112,1,11,1))
if mibBuilder.loadTexts:sunMaxMIB.setRevisions(('2019-11-29 00:00',))
_SunMaxCompliances_ObjectIdentity=ObjectIdentity
sunMaxCompliances=_SunMaxCompliances_ObjectIdentity((1,3,6,1,4,1,41112,1,2,10,1))
_SunMaxGroups_ObjectIdentity=ObjectIdentity
sunMaxGroups=_SunMaxGroups_ObjectIdentity((1,3,6,1,4,1,41112,1,2,10,2))
_SunMaxBatteryStats_ObjectIdentity=ObjectIdentity
sunMaxBatteryStats=_SunMaxBatteryStats_ObjectIdentity((1,3,6,1,4,1,41112,1,11,1,1))
_SunMaxBatCurrent_Type=Integer32
_SunMaxBatCurrent_Object=MibScalar
sunMaxBatCurrent=_SunMaxBatCurrent_Object((1,3,6,1,4,1,41112,1,11,1,1,1),_SunMaxBatCurrent_Type())
sunMaxBatCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxBatCurrent.setStatus(_B)
_SunMaxBatVoltage_Type=Integer32
_SunMaxBatVoltage_Object=MibScalar
sunMaxBatVoltage=_SunMaxBatVoltage_Object((1,3,6,1,4,1,41112,1,11,1,1,2),_SunMaxBatVoltage_Type())
sunMaxBatVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxBatVoltage.setStatus(_B)
_SunMaxBatPower_Type=Integer32
_SunMaxBatPower_Object=MibScalar
sunMaxBatPower=_SunMaxBatPower_Object((1,3,6,1,4,1,41112,1,11,1,1,3),_SunMaxBatPower_Type())
sunMaxBatPower.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxBatPower.setStatus(_B)
_SunMaxBatTemp_Type=Integer32
_SunMaxBatTemp_Object=MibScalar
sunMaxBatTemp=_SunMaxBatTemp_Object((1,3,6,1,4,1,41112,1,11,1,1,4),_SunMaxBatTemp_Type())
sunMaxBatTemp.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxBatTemp.setStatus(_B)
_SunMaxPvPanelStats_ObjectIdentity=ObjectIdentity
sunMaxPvPanelStats=_SunMaxPvPanelStats_ObjectIdentity((1,3,6,1,4,1,41112,1,11,1,2))
_SunMaxPVCurrent_Type=Integer32
_SunMaxPVCurrent_Object=MibScalar
sunMaxPVCurrent=_SunMaxPVCurrent_Object((1,3,6,1,4,1,41112,1,11,1,2,1),_SunMaxPVCurrent_Type())
sunMaxPVCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxPVCurrent.setStatus(_B)
_SunMaxPVVoltage_Type=Integer32
_SunMaxPVVoltage_Object=MibScalar
sunMaxPVVoltage=_SunMaxPVVoltage_Object((1,3,6,1,4,1,41112,1,11,1,2,2),_SunMaxPVVoltage_Type())
sunMaxPVVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxPVVoltage.setStatus(_B)
_SunMaxPVPower_Type=Integer32
_SunMaxPVPower_Object=MibScalar
sunMaxPVPower=_SunMaxPVPower_Object((1,3,6,1,4,1,41112,1,11,1,2,3),_SunMaxPVPower_Type())
sunMaxPVPower.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxPVPower.setStatus(_B)
_SunMaxOutPutStats_ObjectIdentity=ObjectIdentity
sunMaxOutPutStats=_SunMaxOutPutStats_ObjectIdentity((1,3,6,1,4,1,41112,1,11,1,3))
_SunMaxOutCurrent_Type=Integer32
_SunMaxOutCurrent_Object=MibScalar
sunMaxOutCurrent=_SunMaxOutCurrent_Object((1,3,6,1,4,1,41112,1,11,1,3,1),_SunMaxOutCurrent_Type())
sunMaxOutCurrent.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxOutCurrent.setStatus(_B)
_SunMaxOutVoltage_Type=Integer32
_SunMaxOutVoltage_Object=MibScalar
sunMaxOutVoltage=_SunMaxOutVoltage_Object((1,3,6,1,4,1,41112,1,11,1,3,2),_SunMaxOutVoltage_Type())
sunMaxOutVoltage.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxOutVoltage.setStatus(_B)
_SunMaxOutPower_Type=Integer32
_SunMaxOutPower_Object=MibScalar
sunMaxOutPower=_SunMaxOutPower_Object((1,3,6,1,4,1,41112,1,11,1,3,3),_SunMaxOutPower_Type())
sunMaxOutPower.setMaxAccess(_A)
if mibBuilder.loadTexts:sunMaxOutPower.setStatus(_B)
mibBuilder.exportSymbols('UBNT-SUNMAX-MIB',**{'sunMaxCompliances':sunMaxCompliances,'sunMaxGroups':sunMaxGroups,'sunMaxMIB':sunMaxMIB,'sunMaxBatteryStats':sunMaxBatteryStats,'sunMaxBatCurrent':sunMaxBatCurrent,'sunMaxBatVoltage':sunMaxBatVoltage,'sunMaxBatPower':sunMaxBatPower,'sunMaxBatTemp':sunMaxBatTemp,'sunMaxPvPanelStats':sunMaxPvPanelStats,'sunMaxPVCurrent':sunMaxPVCurrent,'sunMaxPVVoltage':sunMaxPVVoltage,'sunMaxPVPower':sunMaxPVPower,'sunMaxOutPutStats':sunMaxOutPutStats,'sunMaxOutCurrent':sunMaxOutCurrent,'sunMaxOutVoltage':sunMaxOutVoltage,'sunMaxOutPower':sunMaxOutPower})