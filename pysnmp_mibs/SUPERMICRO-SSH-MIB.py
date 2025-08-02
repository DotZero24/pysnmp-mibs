_F='Unsigned32'
_E='OctetString'
_D='TruthValue'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
ssh=ModuleIdentity((1,3,6,1,4,1,10876,101,1,97))
if mibBuilder.loadTexts:ssh.setRevisions(('2021-02-19 00:00',))
_SshGeneralGroup_ObjectIdentity=ObjectIdentity
sshGeneralGroup=_SshGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,97,1))
class _SshVersionCompatibility_Type(TruthValue):defaultValue=2
_SshVersionCompatibility_Type.__name__=_D
_SshVersionCompatibility_Object=MibScalar
sshVersionCompatibility=_SshVersionCompatibility_Object((1,3,6,1,4,1,10876,101,1,97,1,1),_SshVersionCompatibility_Type())
sshVersionCompatibility.setMaxAccess(_A)
if mibBuilder.loadTexts:sshVersionCompatibility.setStatus(_B)
class _SshCipherList_Type(Integer32):defaultValue=8189
_SshCipherList_Type.__name__=_C
_SshCipherList_Object=MibScalar
sshCipherList=_SshCipherList_Object((1,3,6,1,4,1,10876,101,1,97,1,2),_SshCipherList_Type())
sshCipherList.setMaxAccess(_A)
if mibBuilder.loadTexts:sshCipherList.setStatus(_B)
class _SshMacList_Type(Integer32):defaultValue=5
_SshMacList_Type.__name__=_C
_SshMacList_Object=MibScalar
sshMacList=_SshMacList_Object((1,3,6,1,4,1,10876,101,1,97,1,3),_SshMacList_Type())
sshMacList.setMaxAccess(_A)
if mibBuilder.loadTexts:sshMacList.setStatus(_B)
_SshTrace_Type=Integer32
_SshTrace_Object=MibScalar
sshTrace=_SshTrace_Object((1,3,6,1,4,1,10876,101,1,97,1,4),_SshTrace_Type())
sshTrace.setMaxAccess(_A)
if mibBuilder.loadTexts:sshTrace.setStatus(_B)
class _SshStatus_Type(TruthValue):defaultValue=1
_SshStatus_Type.__name__=_D
_SshStatus_Object=MibScalar
sshStatus=_SshStatus_Object((1,3,6,1,4,1,10876,101,1,97,1,5),_SshStatus_Type())
sshStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:sshStatus.setStatus(_B)
class _SshTransportMaxAllowedBytes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_SshTransportMaxAllowedBytes_Type.__name__=_C
_SshTransportMaxAllowedBytes_Object=MibScalar
sshTransportMaxAllowedBytes=_SshTransportMaxAllowedBytes_Object((1,3,6,1,4,1,10876,101,1,97,1,6),_SshTransportMaxAllowedBytes_Type())
sshTransportMaxAllowedBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:sshTransportMaxAllowedBytes.setStatus(_B)
class _SshSrvBindAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_SshSrvBindAddr_Type.__name__=_E
_SshSrvBindAddr_Object=MibScalar
sshSrvBindAddr=_SshSrvBindAddr_Object((1,3,6,1,4,1,10876,101,1,97,1,7),_SshSrvBindAddr_Type())
sshSrvBindAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:sshSrvBindAddr.setStatus(_B)
class _SshServerBindPortNo_Type(Unsigned32):defaultValue=22
_SshServerBindPortNo_Type.__name__=_F
_SshServerBindPortNo_Object=MibScalar
sshServerBindPortNo=_SshServerBindPortNo_Object((1,3,6,1,4,1,10876,101,1,97,1,8),_SshServerBindPortNo_Type())
sshServerBindPortNo.setMaxAccess(_A)
if mibBuilder.loadTexts:sshServerBindPortNo.setStatus(_B)
mibBuilder.exportSymbols('SUPERMICRO-SSH-MIB',**{'ssh':ssh,'sshGeneralGroup':sshGeneralGroup,'sshVersionCompatibility':sshVersionCompatibility,'sshCipherList':sshCipherList,'sshMacList':sshMacList,'sshTrace':sshTrace,'sshStatus':sshStatus,'sshTransportMaxAllowedBytes':sshTransportMaxAllowedBytes,'sshSrvBindAddr':sshSrvBindAddr,'sshServerBindPortNo':sshServerBindPortNo})