_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlRCli=ModuleIdentity((1,3,6,1,4,1,4526,17,70))
if mibBuilder.loadTexts:rlRCli.setRevisions(('2007-01-02 00:00',))
_RlRCliMibVersion_Type=Integer32
_RlRCliMibVersion_Object=MibScalar
rlRCliMibVersion=_RlRCliMibVersion_Object((1,3,6,1,4,1,4526,17,70,1),_RlRCliMibVersion_Type())
rlRCliMibVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlRCliMibVersion.setStatus(_A)
class _RlRCliUserPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlRCliUserPassword_Type.__name__=_C
_RlRCliUserPassword_Object=MibScalar
rlRCliUserPassword=_RlRCliUserPassword_Object((1,3,6,1,4,1,4526,17,70,2),_RlRCliUserPassword_Type())
rlRCliUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRCliUserPassword.setStatus(_A)
class _RlRCliEnablePassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlRCliEnablePassword_Type.__name__=_C
_RlRCliEnablePassword_Object=MibScalar
rlRCliEnablePassword=_RlRCliEnablePassword_Object((1,3,6,1,4,1,4526,17,70,3),_RlRCliEnablePassword_Type())
rlRCliEnablePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRCliEnablePassword.setStatus(_A)
class _RlRCliConfigPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlRCliConfigPassword_Type.__name__=_C
_RlRCliConfigPassword_Object=MibScalar
rlRCliConfigPassword=_RlRCliConfigPassword_Object((1,3,6,1,4,1,4526,17,70,4),_RlRCliConfigPassword_Type())
rlRCliConfigPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRCliConfigPassword.setStatus(_A)
class _RlRCliTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_RlRCliTimer_Type.__name__=_D
_RlRCliTimer_Object=MibScalar
rlRCliTimer=_RlRCliTimer_Object((1,3,6,1,4,1,4526,17,70,5),_RlRCliTimer_Type())
rlRCliTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRCliTimer.setStatus(_A)
class _RlRcliFileAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notUsedAfterReset',1),('usedAfterReset',2)))
_RlRcliFileAction_Type.__name__=_D
_RlRcliFileAction_Object=MibScalar
rlRcliFileAction=_RlRcliFileAction_Object((1,3,6,1,4,1,4526,17,70,6),_RlRcliFileAction_Type())
rlRcliFileAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRcliFileAction.setStatus(_A)
mibBuilder.exportSymbols('NETGEAR-RADLAN-RCLI-MIB',**{'rlRCli':rlRCli,'rlRCliMibVersion':rlRCliMibVersion,'rlRCliUserPassword':rlRCliUserPassword,'rlRCliEnablePassword':rlRCliEnablePassword,'rlRCliConfigPassword':rlRCliConfigPassword,'rlRCliTimer':rlRCliTimer,'rlRcliFileAction':rlRcliFileAction})