_I='osCurrentWorkChannel'
_H='NSCRTV-HFCEMS-OPTICALSWITCH-MIB'
_G='commonPhysAddress'
_F='commonNELogicalID'
_E='read-only'
_D='NSCRTV-HFCEMS-COMMON-MIB'
_C='read-write'
_B='mandatory'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
commonNELogicalID,commonPhysAddress=mibBuilder.importSymbols(_D,_F,_G)
nscrtvHFCemsTree,=mibBuilder.importSymbols('NSCRTV-ROOT','nscrtvHFCemsTree')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_OsIdent_ObjectIdentity=ObjectIdentity
osIdent=_OsIdent_ObjectIdentity((1,3,6,1,4,1,17409,1,8686))
_OsVendorOID_Type=ObjectIdentifier
_OsVendorOID_Object=MibScalar
osVendorOID=_OsVendorOID_Object((1,3,6,1,4,1,17409,1,8686,1),_OsVendorOID_Type())
osVendorOID.setMaxAccess(_E)
if mibBuilder.loadTexts:osVendorOID.setStatus('optional')
class _OsWavelength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('1310nm',1),('1490nm',2),('1550nm',3)))
_OsWavelength_Type.__name__=_A
_OsWavelength_Object=MibScalar
osWavelength=_OsWavelength_Object((1,3,6,1,4,1,17409,1,8686,2),_OsWavelength_Type())
osWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:osWavelength.setStatus(_B)
class _OsAutoControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_OsAutoControl_Type.__name__=_A
_OsAutoControl_Object=MibScalar
osAutoControl=_OsAutoControl_Object((1,3,6,1,4,1,17409,1,8686,3),_OsAutoControl_Type())
osAutoControl.setMaxAccess(_C)
if mibBuilder.loadTexts:osAutoControl.setStatus(_B)
class _OsCurrentWorkChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('A',1),('B',2)))
_OsCurrentWorkChannel_Type.__name__=_A
_OsCurrentWorkChannel_Object=MibScalar
osCurrentWorkChannel=_OsCurrentWorkChannel_Object((1,3,6,1,4,1,17409,1,8686,4),_OsCurrentWorkChannel_Type())
osCurrentWorkChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:osCurrentWorkChannel.setStatus(_B)
class _OsSwitchReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-200,300))
_OsSwitchReference_Type.__name__=_A
_OsSwitchReference_Object=MibScalar
osSwitchReference=_OsSwitchReference_Object((1,3,6,1,4,1,17409,1,8686,5),_OsSwitchReference_Type())
osSwitchReference.setMaxAccess(_C)
if mibBuilder.loadTexts:osSwitchReference.setStatus(_B)
class _OsInputOpticalPowerA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_OsInputOpticalPowerA_Type.__name__=_A
_OsInputOpticalPowerA_Object=MibScalar
osInputOpticalPowerA=_OsInputOpticalPowerA_Object((1,3,6,1,4,1,17409,1,8686,6),_OsInputOpticalPowerA_Type())
osInputOpticalPowerA.setMaxAccess(_E)
if mibBuilder.loadTexts:osInputOpticalPowerA.setStatus(_B)
class _OsInputOpticalPowerB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_OsInputOpticalPowerB_Type.__name__=_A
_OsInputOpticalPowerB_Object=MibScalar
osInputOpticalPowerB=_OsInputOpticalPowerB_Object((1,3,6,1,4,1,17409,1,8686,7),_OsInputOpticalPowerB_Type())
osInputOpticalPowerB.setMaxAccess(_E)
if mibBuilder.loadTexts:osInputOpticalPowerB.setStatus(_B)
osSwitchEvent=NotificationType((1,3,6,1,4,1,17409,1,0,8686))
osSwitchEvent.setObjects(*((_D,_G),(_D,_F),(_H,_I)))
if mibBuilder.loadTexts:osSwitchEvent.setStatus('')
mibBuilder.exportSymbols(_H,**{'osSwitchEvent':osSwitchEvent,'osIdent':osIdent,'osVendorOID':osVendorOID,'osWavelength':osWavelength,'osAutoControl':osAutoControl,_I:osCurrentWorkChannel,'osSwitchReference':osSwitchReference,'osInputOpticalPowerA':osInputOpticalPowerA,'osInputOpticalPowerB':osInputOpticalPowerB})