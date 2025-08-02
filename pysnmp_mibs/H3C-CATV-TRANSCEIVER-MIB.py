_H='Integer32'
_G='h3cCATVTransTemperature'
_F='h3cCATVTransOutputLevel'
_E='h3cCATVTransInputPwr'
_D='read-write'
_C='read-only'
_B='H3C-CATV-TRANSCEIVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cCATVTransceiver=ModuleIdentity((1,3,6,1,4,1,2011,10,2,94))
_H3cCATVTransStatus_ObjectIdentity=ObjectIdentity
h3cCATVTransStatus=_H3cCATVTransStatus_ObjectIdentity((1,3,6,1,4,1,2011,10,2,94,1))
_H3cCATVTransStatusScalarObjects_ObjectIdentity=ObjectIdentity
h3cCATVTransStatusScalarObjects=_H3cCATVTransStatusScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,94,1,1))
class _H3cCATVTransState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_H3cCATVTransState_Type.__name__=_H
_H3cCATVTransState_Object=MibScalar
h3cCATVTransState=_H3cCATVTransState_Object((1,3,6,1,4,1,2011,10,2,94,1,1,1),_H3cCATVTransState_Type())
h3cCATVTransState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCATVTransState.setStatus(_A)
_H3cCATVTransInputPwr_Type=Integer32
_H3cCATVTransInputPwr_Object=MibScalar
h3cCATVTransInputPwr=_H3cCATVTransInputPwr_Object((1,3,6,1,4,1,2011,10,2,94,1,1,2),_H3cCATVTransInputPwr_Type())
h3cCATVTransInputPwr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCATVTransInputPwr.setStatus(_A)
if mibBuilder.loadTexts:h3cCATVTransInputPwr.setUnits('dbm')
_H3cCATVTransOutputLevel_Type=Integer32
_H3cCATVTransOutputLevel_Object=MibScalar
h3cCATVTransOutputLevel=_H3cCATVTransOutputLevel_Object((1,3,6,1,4,1,2011,10,2,94,1,1,3),_H3cCATVTransOutputLevel_Type())
h3cCATVTransOutputLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCATVTransOutputLevel.setStatus(_A)
if mibBuilder.loadTexts:h3cCATVTransOutputLevel.setUnits('dbuv')
_H3cCATVTransTemperature_Type=Integer32
_H3cCATVTransTemperature_Object=MibScalar
h3cCATVTransTemperature=_H3cCATVTransTemperature_Object((1,3,6,1,4,1,2011,10,2,94,1,1,4),_H3cCATVTransTemperature_Type())
h3cCATVTransTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cCATVTransTemperature.setStatus(_A)
if mibBuilder.loadTexts:h3cCATVTransTemperature.setUnits('centigrade')
_H3cCATVTransceiverMan_ObjectIdentity=ObjectIdentity
h3cCATVTransceiverMan=_H3cCATVTransceiverMan_ObjectIdentity((1,3,6,1,4,1,2011,10,2,94,2))
_H3cCATVTransCtrlScalarObjects_ObjectIdentity=ObjectIdentity
h3cCATVTransCtrlScalarObjects=_H3cCATVTransCtrlScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,94,2,1))
_H3cCATVTransInputPwrLowerThr_Type=Integer32
_H3cCATVTransInputPwrLowerThr_Object=MibScalar
h3cCATVTransInputPwrLowerThr=_H3cCATVTransInputPwrLowerThr_Object((1,3,6,1,4,1,2011,10,2,94,2,1,1),_H3cCATVTransInputPwrLowerThr_Type())
h3cCATVTransInputPwrLowerThr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cCATVTransInputPwrLowerThr.setStatus(_A)
if mibBuilder.loadTexts:h3cCATVTransInputPwrLowerThr.setUnits('dbm')
_H3cCATVTransOutputLvlLowerThr_Type=Integer32
_H3cCATVTransOutputLvlLowerThr_Object=MibScalar
h3cCATVTransOutputLvlLowerThr=_H3cCATVTransOutputLvlLowerThr_Object((1,3,6,1,4,1,2011,10,2,94,2,1,2),_H3cCATVTransOutputLvlLowerThr_Type())
h3cCATVTransOutputLvlLowerThr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cCATVTransOutputLvlLowerThr.setStatus(_A)
if mibBuilder.loadTexts:h3cCATVTransOutputLvlLowerThr.setUnits('dbuv')
_H3cCATVTransTempratureUpperThr_Type=Integer32
_H3cCATVTransTempratureUpperThr_Object=MibScalar
h3cCATVTransTempratureUpperThr=_H3cCATVTransTempratureUpperThr_Object((1,3,6,1,4,1,2011,10,2,94,2,1,3),_H3cCATVTransTempratureUpperThr_Type())
h3cCATVTransTempratureUpperThr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cCATVTransTempratureUpperThr.setStatus(_A)
_H3cCATVTansTrap_ObjectIdentity=ObjectIdentity
h3cCATVTansTrap=_H3cCATVTansTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,94,3))
_H3cCATVTransTrapPrefix_ObjectIdentity=ObjectIdentity
h3cCATVTransTrapPrefix=_H3cCATVTransTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,94,3,0))
h3cCATVTransInputPwrTrap=NotificationType((1,3,6,1,4,1,2011,10,2,94,3,0,1))
h3cCATVTransInputPwrTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cCATVTransInputPwrTrap.setStatus(_A)
h3cCATVTransInputPwrReTrap=NotificationType((1,3,6,1,4,1,2011,10,2,94,3,0,2))
h3cCATVTransInputPwrReTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:h3cCATVTransInputPwrReTrap.setStatus(_A)
h3cCATVTransOutputLvlTrap=NotificationType((1,3,6,1,4,1,2011,10,2,94,3,0,3))
h3cCATVTransOutputLvlTrap.setObjects((_B,_F))
if mibBuilder.loadTexts:h3cCATVTransOutputLvlTrap.setStatus(_A)
h3cCATVTransOutputLvlReTrap=NotificationType((1,3,6,1,4,1,2011,10,2,94,3,0,4))
h3cCATVTransOutputLvlReTrap.setObjects((_B,_F))
if mibBuilder.loadTexts:h3cCATVTransOutputLvlReTrap.setStatus(_A)
h3cCATVTransTemperatureTrap=NotificationType((1,3,6,1,4,1,2011,10,2,94,3,0,5))
h3cCATVTransTemperatureTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:h3cCATVTransTemperatureTrap.setStatus(_A)
h3cCATVTransTemperatureReTrap=NotificationType((1,3,6,1,4,1,2011,10,2,94,3,0,6))
h3cCATVTransTemperatureReTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:h3cCATVTransTemperatureReTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cCATVTransceiver':h3cCATVTransceiver,'h3cCATVTransStatus':h3cCATVTransStatus,'h3cCATVTransStatusScalarObjects':h3cCATVTransStatusScalarObjects,'h3cCATVTransState':h3cCATVTransState,_E:h3cCATVTransInputPwr,_F:h3cCATVTransOutputLevel,_G:h3cCATVTransTemperature,'h3cCATVTransceiverMan':h3cCATVTransceiverMan,'h3cCATVTransCtrlScalarObjects':h3cCATVTransCtrlScalarObjects,'h3cCATVTransInputPwrLowerThr':h3cCATVTransInputPwrLowerThr,'h3cCATVTransOutputLvlLowerThr':h3cCATVTransOutputLvlLowerThr,'h3cCATVTransTempratureUpperThr':h3cCATVTransTempratureUpperThr,'h3cCATVTansTrap':h3cCATVTansTrap,'h3cCATVTransTrapPrefix':h3cCATVTransTrapPrefix,'h3cCATVTransInputPwrTrap':h3cCATVTransInputPwrTrap,'h3cCATVTransInputPwrReTrap':h3cCATVTransInputPwrReTrap,'h3cCATVTransOutputLvlTrap':h3cCATVTransOutputLvlTrap,'h3cCATVTransOutputLvlReTrap':h3cCATVTransOutputLvlReTrap,'h3cCATVTransTemperatureTrap':h3cCATVTransTemperatureTrap,'h3cCATVTransTemperatureReTrap':h3cCATVTransTemperatureReTrap})