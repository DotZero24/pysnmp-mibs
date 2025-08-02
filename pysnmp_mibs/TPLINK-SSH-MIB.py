_E='enable'
_D='disable'
_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkSshMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,5))
if mibBuilder.loadTexts:tplinkSshMIB.setRevisions(('2012-12-13 09:30',))
_TplinkSshMIBObjects_ObjectIdentity=ObjectIdentity
tplinkSshMIBObjects=_TplinkSshMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,5,1))
class _TpSshEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshEnable_Type.__name__=_A
_TpSshEnable_Object=MibScalar
tpSshEnable=_TpSshEnable_Object((1,3,6,1,4,1,11863,6,5,1,1),_TpSshEnable_Type())
tpSshEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshEnable.setStatus(_C)
class _TpSshProtocolV1Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshProtocolV1Enable_Type.__name__=_A
_TpSshProtocolV1Enable_Object=MibScalar
tpSshProtocolV1Enable=_TpSshProtocolV1Enable_Object((1,3,6,1,4,1,11863,6,5,1,2),_TpSshProtocolV1Enable_Type())
tpSshProtocolV1Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshProtocolV1Enable.setStatus(_C)
class _TpSshProtocolV2Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshProtocolV2Enable_Type.__name__=_A
_TpSshProtocolV2Enable_Object=MibScalar
tpSshProtocolV2Enable=_TpSshProtocolV2Enable_Object((1,3,6,1,4,1,11863,6,5,1,3),_TpSshProtocolV2Enable_Type())
tpSshProtocolV2Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshProtocolV2Enable.setStatus(_C)
class _TpSshSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,360))
_TpSshSessionTimeout_Type.__name__=_A
_TpSshSessionTimeout_Object=MibScalar
tpSshSessionTimeout=_TpSshSessionTimeout_Object((1,3,6,1,4,1,11863,6,5,1,4),_TpSshSessionTimeout_Type())
tpSshSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshSessionTimeout.setStatus(_C)
class _TpSshMaxConnections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TpSshMaxConnections_Type.__name__=_A
_TpSshMaxConnections_Object=MibScalar
tpSshMaxConnections=_TpSshMaxConnections_Object((1,3,6,1,4,1,11863,6,5,1,5),_TpSshMaxConnections_Type())
tpSshMaxConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshMaxConnections.setStatus(_C)
class _TpSshPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpSshPort_Type.__name__=_A
_TpSshPort_Object=MibScalar
tpSshPort=_TpSshPort_Object((1,3,6,1,4,1,11863,6,5,1,6),_TpSshPort_Type())
tpSshPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshPort.setStatus(_C)
class _TpSshEncryptAlgAES128Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshEncryptAlgAES128Enable_Type.__name__=_A
_TpSshEncryptAlgAES128Enable_Object=MibScalar
tpSshEncryptAlgAES128Enable=_TpSshEncryptAlgAES128Enable_Object((1,3,6,1,4,1,11863,6,5,1,7),_TpSshEncryptAlgAES128Enable_Type())
tpSshEncryptAlgAES128Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshEncryptAlgAES128Enable.setStatus(_C)
class _TpSshEncryptAlgAES192Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshEncryptAlgAES192Enable_Type.__name__=_A
_TpSshEncryptAlgAES192Enable_Object=MibScalar
tpSshEncryptAlgAES192Enable=_TpSshEncryptAlgAES192Enable_Object((1,3,6,1,4,1,11863,6,5,1,8),_TpSshEncryptAlgAES192Enable_Type())
tpSshEncryptAlgAES192Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshEncryptAlgAES192Enable.setStatus(_C)
class _TpSshEncryptAlgAES256Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshEncryptAlgAES256Enable_Type.__name__=_A
_TpSshEncryptAlgAES256Enable_Object=MibScalar
tpSshEncryptAlgAES256Enable=_TpSshEncryptAlgAES256Enable_Object((1,3,6,1,4,1,11863,6,5,1,9),_TpSshEncryptAlgAES256Enable_Type())
tpSshEncryptAlgAES256Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshEncryptAlgAES256Enable.setStatus(_C)
class _TpSshEncryptAlgBlowfishEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshEncryptAlgBlowfishEnable_Type.__name__=_A
_TpSshEncryptAlgBlowfishEnable_Object=MibScalar
tpSshEncryptAlgBlowfishEnable=_TpSshEncryptAlgBlowfishEnable_Object((1,3,6,1,4,1,11863,6,5,1,10),_TpSshEncryptAlgBlowfishEnable_Type())
tpSshEncryptAlgBlowfishEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshEncryptAlgBlowfishEnable.setStatus(_C)
class _TpSshEncryptAlgCast128Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshEncryptAlgCast128Enable_Type.__name__=_A
_TpSshEncryptAlgCast128Enable_Object=MibScalar
tpSshEncryptAlgCast128Enable=_TpSshEncryptAlgCast128Enable_Object((1,3,6,1,4,1,11863,6,5,1,11),_TpSshEncryptAlgCast128Enable_Type())
tpSshEncryptAlgCast128Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshEncryptAlgCast128Enable.setStatus(_C)
class _TpSshEncryptAlg3DESEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshEncryptAlg3DESEnable_Type.__name__=_A
_TpSshEncryptAlg3DESEnable_Object=MibScalar
tpSshEncryptAlg3DESEnable=_TpSshEncryptAlg3DESEnable_Object((1,3,6,1,4,1,11863,6,5,1,12),_TpSshEncryptAlg3DESEnable_Type())
tpSshEncryptAlg3DESEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshEncryptAlg3DESEnable.setStatus(_C)
class _TpSshInteAlgSHA1Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshInteAlgSHA1Enable_Type.__name__=_A
_TpSshInteAlgSHA1Enable_Object=MibScalar
tpSshInteAlgSHA1Enable=_TpSshInteAlgSHA1Enable_Object((1,3,6,1,4,1,11863,6,5,1,13),_TpSshInteAlgSHA1Enable_Type())
tpSshInteAlgSHA1Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshInteAlgSHA1Enable.setStatus(_C)
class _TpSshInteAlgMD5Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSshInteAlgMD5Enable_Type.__name__=_A
_TpSshInteAlgMD5Enable_Object=MibScalar
tpSshInteAlgMD5Enable=_TpSshInteAlgMD5Enable_Object((1,3,6,1,4,1,11863,6,5,1,14),_TpSshInteAlgMD5Enable_Type())
tpSshInteAlgMD5Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSshInteAlgMD5Enable.setStatus(_C)
_TplinkSshNotifications_ObjectIdentity=ObjectIdentity
tplinkSshNotifications=_TplinkSshNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,5,2))
mibBuilder.exportSymbols('TPLINK-SSH-MIB',**{'tplinkSshMIB':tplinkSshMIB,'tplinkSshMIBObjects':tplinkSshMIBObjects,'tpSshEnable':tpSshEnable,'tpSshProtocolV1Enable':tpSshProtocolV1Enable,'tpSshProtocolV2Enable':tpSshProtocolV2Enable,'tpSshSessionTimeout':tpSshSessionTimeout,'tpSshMaxConnections':tpSshMaxConnections,'tpSshPort':tpSshPort,'tpSshEncryptAlgAES128Enable':tpSshEncryptAlgAES128Enable,'tpSshEncryptAlgAES192Enable':tpSshEncryptAlgAES192Enable,'tpSshEncryptAlgAES256Enable':tpSshEncryptAlgAES256Enable,'tpSshEncryptAlgBlowfishEnable':tpSshEncryptAlgBlowfishEnable,'tpSshEncryptAlgCast128Enable':tpSshEncryptAlgCast128Enable,'tpSshEncryptAlg3DESEnable':tpSshEncryptAlg3DESEnable,'tpSshInteAlgSHA1Enable':tpSshInteAlgSHA1Enable,'tpSshInteAlgMD5Enable':tpSshInteAlgMD5Enable,'tplinkSshNotifications':tplinkSshNotifications})