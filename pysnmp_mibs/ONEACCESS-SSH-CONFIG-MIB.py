_I='oacSshEnabled'
_H='ONEACCESS-SSH-CONFIG-MIB'
_G='seconds'
_F='TruthValue'
_E='Unsigned32'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oacExpIMIpAcl,oacExpIMManagement,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMIpAcl','oacExpIMManagement','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
oacSshConfigMIB=ModuleIdentity((1,3,6,1,4,1,13191,1,100,2004))
if mibBuilder.loadTexts:oacSshConfigMIB.setRevisions(('2011-07-26 00:00','2011-06-15 00:00'))
_OacSshConfig_ObjectIdentity=ObjectIdentity
oacSshConfig=_OacSshConfig_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,22))
_OacSshConfigObjects_ObjectIdentity=ObjectIdentity
oacSshConfigObjects=_OacSshConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,22,1))
class _OacSshDsaKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,256,512,1024,2048)));namedValues=NamedValues(*(('keysize-0bits',0),('keysize-256bits',256),('keysize-512bits',512),('keysize-1024bits',1024),('keysize-2048bits',2048)))
_OacSshDsaKey_Type.__name__=_C
_OacSshDsaKey_Object=MibScalar
oacSshDsaKey=_OacSshDsaKey_Object((1,3,6,1,4,1,13191,10,3,4,22,1,1),_OacSshDsaKey_Type())
oacSshDsaKey.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSshDsaKey.setStatus(_A)
class _OacSshEnabled_Type(TruthValue):defaultValue=2
_OacSshEnabled_Type.__name__=_F
_OacSshEnabled_Object=MibScalar
oacSshEnabled=_OacSshEnabled_Object((1,3,6,1,4,1,13191,10,3,4,22,1,2),_OacSshEnabled_Type())
oacSshEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSshEnabled.setStatus(_A)
class _OacSshIdleTimeout_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,4294967295))
_OacSshIdleTimeout_Type.__name__=_E
_OacSshIdleTimeout_Object=MibScalar
oacSshIdleTimeout=_OacSshIdleTimeout_Object((1,3,6,1,4,1,13191,10,3,4,22,1,3),_OacSshIdleTimeout_Type())
oacSshIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSshIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:oacSshIdleTimeout.setUnits(_G)
class _OacSshAuthTimeout_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,120))
_OacSshAuthTimeout_Type.__name__=_C
_OacSshAuthTimeout_Object=MibScalar
oacSshAuthTimeout=_OacSshAuthTimeout_Object((1,3,6,1,4,1,13191,10,3,4,22,1,4),_OacSshAuthTimeout_Type())
oacSshAuthTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSshAuthTimeout.setStatus(_A)
if mibBuilder.loadTexts:oacSshAuthTimeout.setUnits(_G)
class _OacSshAuthRetries_Type(Integer32):defaultValue=3
_OacSshAuthRetries_Type.__name__=_C
_OacSshAuthRetries_Object=MibScalar
oacSshAuthRetries=_OacSshAuthRetries_Object((1,3,6,1,4,1,13191,10,3,4,22,1,5),_OacSshAuthRetries_Type())
oacSshAuthRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSshAuthRetries.setStatus(_A)
class _OacSshBindInterface_Type(OctetString):defaultValue=OctetString('any');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OacSshBindInterface_Type.__name__=_D
_OacSshBindInterface_Object=MibScalar
oacSshBindInterface=_OacSshBindInterface_Object((1,3,6,1,4,1,13191,10,3,4,22,1,6),_OacSshBindInterface_Type())
oacSshBindInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSshBindInterface.setStatus(_A)
class _OacSshBindAcl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSshBindAcl_Type.__name__=_D
_OacSshBindAcl_Object=MibScalar
oacSshBindAcl=_OacSshBindAcl_Object((1,3,6,1,4,1,13191,10,3,4,22,1,7),_OacSshBindAcl_Type())
oacSshBindAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSshBindAcl.setStatus(_A)
class _OacSshMaxSessions_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_OacSshMaxSessions_Type.__name__=_C
_OacSshMaxSessions_Object=MibScalar
oacSshMaxSessions=_OacSshMaxSessions_Object((1,3,6,1,4,1,13191,10,3,4,22,1,8),_OacSshMaxSessions_Type())
oacSshMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSshMaxSessions.setStatus(_A)
class _OacSshMaxSessionChannels_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_OacSshMaxSessionChannels_Type.__name__=_C
_OacSshMaxSessionChannels_Object=MibScalar
oacSshMaxSessionChannels=_OacSshMaxSessionChannels_Object((1,3,6,1,4,1,13191,10,3,4,22,1,9),_OacSshMaxSessionChannels_Type())
oacSshMaxSessionChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSshMaxSessionChannels.setStatus(_A)
_OacSshConfigConformance_ObjectIdentity=ObjectIdentity
oacSshConfigConformance=_OacSshConfigConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,22,2))
_OacSshConfigGroups_ObjectIdentity=ObjectIdentity
oacSshConfigGroups=_OacSshConfigGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,22,2,1))
_OacSshCompls_ObjectIdentity=ObjectIdentity
oacSshCompls=_OacSshCompls_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,22,2,2))
oacSshConfigGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,4,22,2,1,1))
oacSshConfigGroup.setObjects((_H,_I))
if mibBuilder.loadTexts:oacSshConfigGroup.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'oacSshConfigMIB':oacSshConfigMIB,'oacSshConfig':oacSshConfig,'oacSshConfigObjects':oacSshConfigObjects,'oacSshDsaKey':oacSshDsaKey,_I:oacSshEnabled,'oacSshIdleTimeout':oacSshIdleTimeout,'oacSshAuthTimeout':oacSshAuthTimeout,'oacSshAuthRetries':oacSshAuthRetries,'oacSshBindInterface':oacSshBindInterface,'oacSshBindAcl':oacSshBindAcl,'oacSshMaxSessions':oacSshMaxSessions,'oacSshMaxSessionChannels':oacSshMaxSessionChannels,'oacSshConfigConformance':oacSshConfigConformance,'oacSshConfigGroups':oacSshConfigGroups,'oacSshConfigGroup':oacSshConfigGroup,'oacSshCompls':oacSshCompls})