_P='Unsigned32'
_O='MibTableColumn'
_N='MibTableRow'
_M='MibTable'
_L='MibScalar'
_K='ObjectIdentity'
_J='NotificationType'
_I='ModuleIdentity'
_H='NOTLOCKED'
_G='LOCKED'
_F='ENABLED'
_E='DISABLED'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress',_I,'MibIdentifier',_J,_K,_L,_M,_N,_O,'Opaque','TimeTicks',_P,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ModuleIdentity,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Unsigned32,apex=mibBuilder.importSymbols('TRANGO-APEX-MIB',_I,_J,_K,_L,_M,_N,_O,_P,'apex')
_Modem_ObjectIdentity=ObjectIdentity
modem=_Modem_ObjectIdentity((1,3,6,1,4,1,5454,1,60,2))
class _ModemLoopbackMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('OFF',0),('DIGITAL',1),('IF',2),('RFGEN',3),('RFREFL',4)))
_ModemLoopbackMode_Type.__name__=_C
_ModemLoopbackMode_Object=MibScalar
modemLoopbackMode=_ModemLoopbackMode_Object((1,3,6,1,4,1,5454,1,60,2,1),_ModemLoopbackMode_Type())
modemLoopbackMode.setMaxAccess(_B)
if mibBuilder.loadTexts:modemLoopbackMode.setStatus(_A)
class _ModemDataPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('EXT',0),('INT',1)))
_ModemDataPattern_Type.__name__=_C
_ModemDataPattern_Object=MibScalar
modemDataPattern=_ModemDataPattern_Object((1,3,6,1,4,1,5454,1,60,2,2),_ModemDataPattern_Type())
modemDataPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:modemDataPattern.setStatus(_A)
_ModemBER_Type=DisplayString
_ModemBER_Object=MibScalar
modemBER=_ModemBER_Object((1,3,6,1,4,1,5454,1,60,2,3),_ModemBER_Type())
modemBER.setMaxAccess(_D)
if mibBuilder.loadTexts:modemBER.setStatus(_A)
_ModemMSE_Type=Integer32
_ModemMSE_Object=MibScalar
modemMSE=_ModemMSE_Object((1,3,6,1,4,1,5454,1,60,2,4),_ModemMSE_Type())
modemMSE.setMaxAccess(_D)
if mibBuilder.loadTexts:modemMSE.setStatus(_A)
_ModemFER_Type=DisplayString
_ModemFER_Object=MibScalar
modemFER=_ModemFER_Object((1,3,6,1,4,1,5454,1,60,2,5),_ModemFER_Type())
modemFER.setMaxAccess(_D)
if mibBuilder.loadTexts:modemFER.setStatus(_A)
_Lock_ObjectIdentity=ObjectIdentity
lock=_Lock_ObjectIdentity((1,3,6,1,4,1,5454,1,60,2,6))
class _ModemLockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('UNLOCKED',0),(_G,1),('PROGRESS',2)))
_ModemLockStatus_Type.__name__=_C
_ModemLockStatus_Object=MibScalar
modemLockStatus=_ModemLockStatus_Object((1,3,6,1,4,1,5454,1,60,2,6,1),_ModemLockStatus_Type())
modemLockStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:modemLockStatus.setStatus(_A)
class _ModemTimingLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_ModemTimingLock_Type.__name__=_C
_ModemTimingLock_Object=MibScalar
modemTimingLock=_ModemTimingLock_Object((1,3,6,1,4,1,5454,1,60,2,6,2),_ModemTimingLock_Type())
modemTimingLock.setMaxAccess(_D)
if mibBuilder.loadTexts:modemTimingLock.setStatus(_A)
class _ModemPreambleLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_ModemPreambleLock_Type.__name__=_C
_ModemPreambleLock_Object=MibScalar
modemPreambleLock=_ModemPreambleLock_Object((1,3,6,1,4,1,5454,1,60,2,6,3),_ModemPreambleLock_Type())
modemPreambleLock.setMaxAccess(_D)
if mibBuilder.loadTexts:modemPreambleLock.setStatus(_A)
class _ModemLdpcLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_ModemLdpcLock_Type.__name__=_C
_ModemLdpcLock_Object=MibScalar
modemLdpcLock=_ModemLdpcLock_Object((1,3,6,1,4,1,5454,1,60,2,6,4),_ModemLdpcLock_Type())
modemLdpcLock.setMaxAccess(_D)
if mibBuilder.loadTexts:modemLdpcLock.setStatus(_A)
_ModemReserved_Type=Integer32
_ModemReserved_Object=MibScalar
modemReserved=_ModemReserved_Object((1,3,6,1,4,1,5454,1,60,2,6,5),_ModemReserved_Type())
modemReserved.setMaxAccess(_D)
if mibBuilder.loadTexts:modemReserved.setStatus(_A)
_Acm_ObjectIdentity=ObjectIdentity
acm=_Acm_ObjectIdentity((1,3,6,1,4,1,5454,1,60,2,7))
class _ModemACMEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ModemACMEnable_Type.__name__=_C
_ModemACMEnable_Object=MibScalar
modemACMEnable=_ModemACMEnable_Object((1,3,6,1,4,1,5454,1,60,2,7,1),_ModemACMEnable_Type())
modemACMEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMEnable.setStatus(_A)
_Acmprofile_ObjectIdentity=ObjectIdentity
acmprofile=_Acmprofile_ObjectIdentity((1,3,6,1,4,1,5454,1,60,2,7,2))
class _ModemACMProfileQPSKEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ModemACMProfileQPSKEnable_Type.__name__=_C
_ModemACMProfileQPSKEnable_Object=MibScalar
modemACMProfileQPSKEnable=_ModemACMProfileQPSKEnable_Object((1,3,6,1,4,1,5454,1,60,2,7,2,1),_ModemACMProfileQPSKEnable_Type())
modemACMProfileQPSKEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMProfileQPSKEnable.setStatus(_A)
class _ModemACMProfileQAM16Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ModemACMProfileQAM16Enable_Type.__name__=_C
_ModemACMProfileQAM16Enable_Object=MibScalar
modemACMProfileQAM16Enable=_ModemACMProfileQAM16Enable_Object((1,3,6,1,4,1,5454,1,60,2,7,2,2),_ModemACMProfileQAM16Enable_Type())
modemACMProfileQAM16Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMProfileQAM16Enable.setStatus(_A)
class _ModemACMProfileQAM32Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ModemACMProfileQAM32Enable_Type.__name__=_C
_ModemACMProfileQAM32Enable_Object=MibScalar
modemACMProfileQAM32Enable=_ModemACMProfileQAM32Enable_Object((1,3,6,1,4,1,5454,1,60,2,7,2,3),_ModemACMProfileQAM32Enable_Type())
modemACMProfileQAM32Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMProfileQAM32Enable.setStatus(_A)
class _ModemACMProfileQAM64Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ModemACMProfileQAM64Enable_Type.__name__=_C
_ModemACMProfileQAM64Enable_Object=MibScalar
modemACMProfileQAM64Enable=_ModemACMProfileQAM64Enable_Object((1,3,6,1,4,1,5454,1,60,2,7,2,4),_ModemACMProfileQAM64Enable_Type())
modemACMProfileQAM64Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMProfileQAM64Enable.setStatus(_A)
class _ModemACMProfileQAM128Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ModemACMProfileQAM128Enable_Type.__name__=_C
_ModemACMProfileQAM128Enable_Object=MibScalar
modemACMProfileQAM128Enable=_ModemACMProfileQAM128Enable_Object((1,3,6,1,4,1,5454,1,60,2,7,2,5),_ModemACMProfileQAM128Enable_Type())
modemACMProfileQAM128Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMProfileQAM128Enable.setStatus(_A)
class _ModemACMProfileQAM256Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ModemACMProfileQAM256Enable_Type.__name__=_C
_ModemACMProfileQAM256Enable_Object=MibScalar
modemACMProfileQAM256Enable=_ModemACMProfileQAM256Enable_Object((1,3,6,1,4,1,5454,1,60,2,7,2,6),_ModemACMProfileQAM256Enable_Type())
modemACMProfileQAM256Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMProfileQAM256Enable.setStatus(_A)
_AcmMSEImprove_ObjectIdentity=ObjectIdentity
acmMSEImprove=_AcmMSEImprove_ObjectIdentity((1,3,6,1,4,1,5454,1,60,2,7,3))
_ModemACMQPSKMSEImprove_Type=Opaque
_ModemACMQPSKMSEImprove_Object=MibScalar
modemACMQPSKMSEImprove=_ModemACMQPSKMSEImprove_Object((1,3,6,1,4,1,5454,1,60,2,7,3,1),_ModemACMQPSKMSEImprove_Type())
modemACMQPSKMSEImprove.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQPSKMSEImprove.setStatus(_A)
_ModemACMQAM16MSEImprove_Type=Opaque
_ModemACMQAM16MSEImprove_Object=MibScalar
modemACMQAM16MSEImprove=_ModemACMQAM16MSEImprove_Object((1,3,6,1,4,1,5454,1,60,2,7,3,2),_ModemACMQAM16MSEImprove_Type())
modemACMQAM16MSEImprove.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM16MSEImprove.setStatus(_A)
_ModemACMQAM32MSEImprove_Type=Opaque
_ModemACMQAM32MSEImprove_Object=MibScalar
modemACMQAM32MSEImprove=_ModemACMQAM32MSEImprove_Object((1,3,6,1,4,1,5454,1,60,2,7,3,3),_ModemACMQAM32MSEImprove_Type())
modemACMQAM32MSEImprove.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM32MSEImprove.setStatus(_A)
_ModemACMQAM64MSEImprove_Type=Opaque
_ModemACMQAM64MSEImprove_Object=MibScalar
modemACMQAM64MSEImprove=_ModemACMQAM64MSEImprove_Object((1,3,6,1,4,1,5454,1,60,2,7,3,4),_ModemACMQAM64MSEImprove_Type())
modemACMQAM64MSEImprove.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM64MSEImprove.setStatus(_A)
_ModemACMQAM128MSEImprove_Type=Opaque
_ModemACMQAM128MSEImprove_Object=MibScalar
modemACMQAM128MSEImprove=_ModemACMQAM128MSEImprove_Object((1,3,6,1,4,1,5454,1,60,2,7,3,5),_ModemACMQAM128MSEImprove_Type())
modemACMQAM128MSEImprove.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM128MSEImprove.setStatus(_A)
_ModemACMQAM256MSEImprove_Type=Opaque
_ModemACMQAM256MSEImprove_Object=MibScalar
modemACMQAM256MSEImprove=_ModemACMQAM256MSEImprove_Object((1,3,6,1,4,1,5454,1,60,2,7,3,6),_ModemACMQAM256MSEImprove_Type())
modemACMQAM256MSEImprove.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM256MSEImprove.setStatus(_A)
_AcmMSEDegrade_ObjectIdentity=ObjectIdentity
acmMSEDegrade=_AcmMSEDegrade_ObjectIdentity((1,3,6,1,4,1,5454,1,60,2,7,4))
_ModemACMQPSKMSEDegrade_Type=Opaque
_ModemACMQPSKMSEDegrade_Object=MibScalar
modemACMQPSKMSEDegrade=_ModemACMQPSKMSEDegrade_Object((1,3,6,1,4,1,5454,1,60,2,7,4,1),_ModemACMQPSKMSEDegrade_Type())
modemACMQPSKMSEDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQPSKMSEDegrade.setStatus(_A)
_ModemACMQAM16MSEDegrade_Type=Opaque
_ModemACMQAM16MSEDegrade_Object=MibScalar
modemACMQAM16MSEDegrade=_ModemACMQAM16MSEDegrade_Object((1,3,6,1,4,1,5454,1,60,2,7,4,2),_ModemACMQAM16MSEDegrade_Type())
modemACMQAM16MSEDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM16MSEDegrade.setStatus(_A)
_ModemACMQAM32MSEDegrade_Type=Opaque
_ModemACMQAM32MSEDegrade_Object=MibScalar
modemACMQAM32MSEDegrade=_ModemACMQAM32MSEDegrade_Object((1,3,6,1,4,1,5454,1,60,2,7,4,3),_ModemACMQAM32MSEDegrade_Type())
modemACMQAM32MSEDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM32MSEDegrade.setStatus(_A)
_ModemACMQAM64MSEDegrade_Type=Opaque
_ModemACMQAM64MSEDegrade_Object=MibScalar
modemACMQAM64MSEDegrade=_ModemACMQAM64MSEDegrade_Object((1,3,6,1,4,1,5454,1,60,2,7,4,4),_ModemACMQAM64MSEDegrade_Type())
modemACMQAM64MSEDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM64MSEDegrade.setStatus(_A)
_ModemACMQAM128MSEDegrade_Type=Opaque
_ModemACMQAM128MSEDegrade_Object=MibScalar
modemACMQAM128MSEDegrade=_ModemACMQAM128MSEDegrade_Object((1,3,6,1,4,1,5454,1,60,2,7,4,5),_ModemACMQAM128MSEDegrade_Type())
modemACMQAM128MSEDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM128MSEDegrade.setStatus(_A)
_ModemACMQAM256MSEDegrade_Type=Opaque
_ModemACMQAM256MSEDegrade_Object=MibScalar
modemACMQAM256MSEDegrade=_ModemACMQAM256MSEDegrade_Object((1,3,6,1,4,1,5454,1,60,2,7,4,6),_ModemACMQAM256MSEDegrade_Type())
modemACMQAM256MSEDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMQAM256MSEDegrade.setStatus(_A)
_Profile_ObjectIdentity=ObjectIdentity
profile=_Profile_ObjectIdentity((1,3,6,1,4,1,5454,1,60,2,8))
_ModemACMTxProfile_Type=Integer32
_ModemACMTxProfile_Object=MibScalar
modemACMTxProfile=_ModemACMTxProfile_Object((1,3,6,1,4,1,5454,1,60,2,8,1),_ModemACMTxProfile_Type())
modemACMTxProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMTxProfile.setStatus(_A)
_ModemACMRxProfile_Type=Integer32
_ModemACMRxProfile_Object=MibScalar
modemACMRxProfile=_ModemACMRxProfile_Object((1,3,6,1,4,1,5454,1,60,2,8,2),_ModemACMRxProfile_Type())
modemACMRxProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:modemACMRxProfile.setStatus(_A)
mibBuilder.exportSymbols('TRANGO-APEX-MODEM-MIB',**{'modem':modem,'modemLoopbackMode':modemLoopbackMode,'modemDataPattern':modemDataPattern,'modemBER':modemBER,'modemMSE':modemMSE,'modemFER':modemFER,'lock':lock,'modemLockStatus':modemLockStatus,'modemTimingLock':modemTimingLock,'modemPreambleLock':modemPreambleLock,'modemLdpcLock':modemLdpcLock,'modemReserved':modemReserved,'acm':acm,'modemACMEnable':modemACMEnable,'acmprofile':acmprofile,'modemACMProfileQPSKEnable':modemACMProfileQPSKEnable,'modemACMProfileQAM16Enable':modemACMProfileQAM16Enable,'modemACMProfileQAM32Enable':modemACMProfileQAM32Enable,'modemACMProfileQAM64Enable':modemACMProfileQAM64Enable,'modemACMProfileQAM128Enable':modemACMProfileQAM128Enable,'modemACMProfileQAM256Enable':modemACMProfileQAM256Enable,'acmMSEImprove':acmMSEImprove,'modemACMQPSKMSEImprove':modemACMQPSKMSEImprove,'modemACMQAM16MSEImprove':modemACMQAM16MSEImprove,'modemACMQAM32MSEImprove':modemACMQAM32MSEImprove,'modemACMQAM64MSEImprove':modemACMQAM64MSEImprove,'modemACMQAM128MSEImprove':modemACMQAM128MSEImprove,'modemACMQAM256MSEImprove':modemACMQAM256MSEImprove,'acmMSEDegrade':acmMSEDegrade,'modemACMQPSKMSEDegrade':modemACMQPSKMSEDegrade,'modemACMQAM16MSEDegrade':modemACMQAM16MSEDegrade,'modemACMQAM32MSEDegrade':modemACMQAM32MSEDegrade,'modemACMQAM64MSEDegrade':modemACMQAM64MSEDegrade,'modemACMQAM128MSEDegrade':modemACMQAM128MSEDegrade,'modemACMQAM256MSEDegrade':modemACMQAM256MSEDegrade,'profile':profile,'modemACMTxProfile':modemACMTxProfile,'modemACMRxProfile':modemACMRxProfile})