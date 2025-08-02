_H='Integer32'
_G='hpnicfCATVTransTemperature'
_F='hpnicfCATVTransOutputLevel'
_E='hpnicfCATVTransInputPwr'
_D='read-write'
_C='read-only'
_B='HPN-ICF-CATV-TRANSCEIVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfCATVTransceiver=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,94))
_HpnicfCATVTransStatus_ObjectIdentity=ObjectIdentity
hpnicfCATVTransStatus=_HpnicfCATVTransStatus_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,94,1))
_HpnicfCATVTransStatusScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfCATVTransStatusScalarObjects=_HpnicfCATVTransStatusScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,94,1,1))
class _HpnicfCATVTransState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_HpnicfCATVTransState_Type.__name__=_H
_HpnicfCATVTransState_Object=MibScalar
hpnicfCATVTransState=_HpnicfCATVTransState_Object((1,3,6,1,4,1,11,2,14,11,15,2,94,1,1,1),_HpnicfCATVTransState_Type())
hpnicfCATVTransState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCATVTransState.setStatus(_A)
_HpnicfCATVTransInputPwr_Type=Integer32
_HpnicfCATVTransInputPwr_Object=MibScalar
hpnicfCATVTransInputPwr=_HpnicfCATVTransInputPwr_Object((1,3,6,1,4,1,11,2,14,11,15,2,94,1,1,2),_HpnicfCATVTransInputPwr_Type())
hpnicfCATVTransInputPwr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCATVTransInputPwr.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCATVTransInputPwr.setUnits('dbm')
_HpnicfCATVTransOutputLevel_Type=Integer32
_HpnicfCATVTransOutputLevel_Object=MibScalar
hpnicfCATVTransOutputLevel=_HpnicfCATVTransOutputLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,94,1,1,3),_HpnicfCATVTransOutputLevel_Type())
hpnicfCATVTransOutputLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCATVTransOutputLevel.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCATVTransOutputLevel.setUnits('dbuv')
_HpnicfCATVTransTemperature_Type=Integer32
_HpnicfCATVTransTemperature_Object=MibScalar
hpnicfCATVTransTemperature=_HpnicfCATVTransTemperature_Object((1,3,6,1,4,1,11,2,14,11,15,2,94,1,1,4),_HpnicfCATVTransTemperature_Type())
hpnicfCATVTransTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCATVTransTemperature.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCATVTransTemperature.setUnits('centigrade')
_HpnicfCATVTransceiverMan_ObjectIdentity=ObjectIdentity
hpnicfCATVTransceiverMan=_HpnicfCATVTransceiverMan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,94,2))
_HpnicfCATVTransCtrlScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfCATVTransCtrlScalarObjects=_HpnicfCATVTransCtrlScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,94,2,1))
_HpnicfCATVTransInputPwrLowerThr_Type=Integer32
_HpnicfCATVTransInputPwrLowerThr_Object=MibScalar
hpnicfCATVTransInputPwrLowerThr=_HpnicfCATVTransInputPwrLowerThr_Object((1,3,6,1,4,1,11,2,14,11,15,2,94,2,1,1),_HpnicfCATVTransInputPwrLowerThr_Type())
hpnicfCATVTransInputPwrLowerThr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCATVTransInputPwrLowerThr.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCATVTransInputPwrLowerThr.setUnits('dbm')
_HpnicfCATVTransOutputLvlLowerThr_Type=Integer32
_HpnicfCATVTransOutputLvlLowerThr_Object=MibScalar
hpnicfCATVTransOutputLvlLowerThr=_HpnicfCATVTransOutputLvlLowerThr_Object((1,3,6,1,4,1,11,2,14,11,15,2,94,2,1,2),_HpnicfCATVTransOutputLvlLowerThr_Type())
hpnicfCATVTransOutputLvlLowerThr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCATVTransOutputLvlLowerThr.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCATVTransOutputLvlLowerThr.setUnits('dbuv')
_HpnicfCATVTransTempratureUpperThr_Type=Integer32
_HpnicfCATVTransTempratureUpperThr_Object=MibScalar
hpnicfCATVTransTempratureUpperThr=_HpnicfCATVTransTempratureUpperThr_Object((1,3,6,1,4,1,11,2,14,11,15,2,94,2,1,3),_HpnicfCATVTransTempratureUpperThr_Type())
hpnicfCATVTransTempratureUpperThr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCATVTransTempratureUpperThr.setStatus(_A)
_HpnicfCATVTansTrap_ObjectIdentity=ObjectIdentity
hpnicfCATVTansTrap=_HpnicfCATVTansTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,94,3))
_HpnicfCATVTransTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfCATVTransTrapPrefix=_HpnicfCATVTransTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,94,3,0))
hpnicfCATVTransInputPwrTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,94,3,0,1))
hpnicfCATVTransInputPwrTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:hpnicfCATVTransInputPwrTrap.setStatus(_A)
hpnicfCATVTransInputPwrReTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,94,3,0,2))
hpnicfCATVTransInputPwrReTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:hpnicfCATVTransInputPwrReTrap.setStatus(_A)
hpnicfCATVTransOutputLvlTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,94,3,0,3))
hpnicfCATVTransOutputLvlTrap.setObjects((_B,_F))
if mibBuilder.loadTexts:hpnicfCATVTransOutputLvlTrap.setStatus(_A)
hpnicfCATVTransOutputLvlReTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,94,3,0,4))
hpnicfCATVTransOutputLvlReTrap.setObjects((_B,_F))
if mibBuilder.loadTexts:hpnicfCATVTransOutputLvlReTrap.setStatus(_A)
hpnicfCATVTransTemperatureTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,94,3,0,5))
hpnicfCATVTransTemperatureTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:hpnicfCATVTransTemperatureTrap.setStatus(_A)
hpnicfCATVTransTemperatureReTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,94,3,0,6))
hpnicfCATVTransTemperatureReTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:hpnicfCATVTransTemperatureReTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfCATVTransceiver':hpnicfCATVTransceiver,'hpnicfCATVTransStatus':hpnicfCATVTransStatus,'hpnicfCATVTransStatusScalarObjects':hpnicfCATVTransStatusScalarObjects,'hpnicfCATVTransState':hpnicfCATVTransState,_E:hpnicfCATVTransInputPwr,_F:hpnicfCATVTransOutputLevel,_G:hpnicfCATVTransTemperature,'hpnicfCATVTransceiverMan':hpnicfCATVTransceiverMan,'hpnicfCATVTransCtrlScalarObjects':hpnicfCATVTransCtrlScalarObjects,'hpnicfCATVTransInputPwrLowerThr':hpnicfCATVTransInputPwrLowerThr,'hpnicfCATVTransOutputLvlLowerThr':hpnicfCATVTransOutputLvlLowerThr,'hpnicfCATVTransTempratureUpperThr':hpnicfCATVTransTempratureUpperThr,'hpnicfCATVTansTrap':hpnicfCATVTansTrap,'hpnicfCATVTransTrapPrefix':hpnicfCATVTransTrapPrefix,'hpnicfCATVTransInputPwrTrap':hpnicfCATVTransInputPwrTrap,'hpnicfCATVTransInputPwrReTrap':hpnicfCATVTransInputPwrReTrap,'hpnicfCATVTransOutputLvlTrap':hpnicfCATVTransOutputLvlTrap,'hpnicfCATVTransOutputLvlReTrap':hpnicfCATVTransOutputLvlReTrap,'hpnicfCATVTransTemperatureTrap':hpnicfCATVTransTemperatureTrap,'hpnicfCATVTransTemperatureReTrap':hpnicfCATVTransTemperatureReTrap})