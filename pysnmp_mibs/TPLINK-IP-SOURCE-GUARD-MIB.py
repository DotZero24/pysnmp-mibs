_H='read-only'
_G='read-write'
_F='disable'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkIpSourceGuardMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,29))
if mibBuilder.loadTexts:tplinkIpSourceGuardMIB.setRevisions(('2012-12-13 09:30',))
_TplinkIpSourceGuardMIBObjects_ObjectIdentity=ObjectIdentity
tplinkIpSourceGuardMIBObjects=_TplinkIpSourceGuardMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,29,1))
_TpIpSourceGuardConfig_ObjectIdentity=ObjectIdentity
tpIpSourceGuardConfig=_TpIpSourceGuardConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,29,1,1))
class _TpIpSourceGuardLoggingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('enable',1)))
_TpIpSourceGuardLoggingConfig_Type.__name__=_C
_TpIpSourceGuardLoggingConfig_Object=MibScalar
tpIpSourceGuardLoggingConfig=_TpIpSourceGuardLoggingConfig_Object((1,3,6,1,4,1,11863,6,29,1,1,1),_TpIpSourceGuardLoggingConfig_Type())
tpIpSourceGuardLoggingConfig.setMaxAccess(_G)
if mibBuilder.loadTexts:tpIpSourceGuardLoggingConfig.setStatus(_A)
_TpIpSourceGuardConfigTable_Object=MibTable
tpIpSourceGuardConfigTable=_TpIpSourceGuardConfigTable_Object((1,3,6,1,4,1,11863,6,29,1,1,2))
if mibBuilder.loadTexts:tpIpSourceGuardConfigTable.setStatus(_A)
_TpIpSourceGuardConfigEntry_Object=MibTableRow
tpIpSourceGuardConfigEntry=_TpIpSourceGuardConfigEntry_Object((1,3,6,1,4,1,11863,6,29,1,1,2,1))
tpIpSourceGuardConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tpIpSourceGuardConfigEntry.setStatus(_A)
class _TpIpSourceGuardConfigPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpIpSourceGuardConfigPort_Type.__name__=_B
_TpIpSourceGuardConfigPort_Object=MibTableColumn
tpIpSourceGuardConfigPort=_TpIpSourceGuardConfigPort_Object((1,3,6,1,4,1,11863,6,29,1,1,2,1,1),_TpIpSourceGuardConfigPort_Type())
tpIpSourceGuardConfigPort.setMaxAccess(_H)
if mibBuilder.loadTexts:tpIpSourceGuardConfigPort.setStatus(_A)
class _TpIpSourceGuardConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('sip',1),('sip-mac',2)))
_TpIpSourceGuardConfigType_Type.__name__=_C
_TpIpSourceGuardConfigType_Object=MibTableColumn
tpIpSourceGuardConfigType=_TpIpSourceGuardConfigType_Object((1,3,6,1,4,1,11863,6,29,1,1,2,1,2),_TpIpSourceGuardConfigType_Type())
tpIpSourceGuardConfigType.setMaxAccess(_G)
if mibBuilder.loadTexts:tpIpSourceGuardConfigType.setStatus(_A)
class _TpIpSourceGuardConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpIpSourceGuardConfigPortLag_Type.__name__=_B
_TpIpSourceGuardConfigPortLag_Object=MibTableColumn
tpIpSourceGuardConfigPortLag=_TpIpSourceGuardConfigPortLag_Object((1,3,6,1,4,1,11863,6,29,1,1,2,1,3),_TpIpSourceGuardConfigPortLag_Type())
tpIpSourceGuardConfigPortLag.setMaxAccess(_H)
if mibBuilder.loadTexts:tpIpSourceGuardConfigPortLag.setStatus(_A)
_TplinkIpSourceGuardNotifications_ObjectIdentity=ObjectIdentity
tplinkIpSourceGuardNotifications=_TplinkIpSourceGuardNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,29,2))
tpIpSourceGuardRxIllegalIpPacket=NotificationType((1,3,6,1,4,1,11863,6,29,2,1))
if mibBuilder.loadTexts:tpIpSourceGuardRxIllegalIpPacket.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-IP-SOURCE-GUARD-MIB',**{'tplinkIpSourceGuardMIB':tplinkIpSourceGuardMIB,'tplinkIpSourceGuardMIBObjects':tplinkIpSourceGuardMIBObjects,'tpIpSourceGuardConfig':tpIpSourceGuardConfig,'tpIpSourceGuardLoggingConfig':tpIpSourceGuardLoggingConfig,'tpIpSourceGuardConfigTable':tpIpSourceGuardConfigTable,'tpIpSourceGuardConfigEntry':tpIpSourceGuardConfigEntry,'tpIpSourceGuardConfigPort':tpIpSourceGuardConfigPort,'tpIpSourceGuardConfigType':tpIpSourceGuardConfigType,'tpIpSourceGuardConfigPortLag':tpIpSourceGuardConfigPortLag,'tplinkIpSourceGuardNotifications':tplinkIpSourceGuardNotifications,'tpIpSourceGuardRxIllegalIpPacket':tpIpSourceGuardRxIllegalIpPacket})