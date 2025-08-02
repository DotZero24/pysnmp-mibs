_D='disabled'
_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ruckusCommonL2TPModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonL2TPModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ruckusL2TPMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,14,1))
_RuckusL2TPObjects_ObjectIdentity=ObjectIdentity
ruckusL2TPObjects=_RuckusL2TPObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,14,1,1))
_RuckusL2TPInfo_ObjectIdentity=ObjectIdentity
ruckusL2TPInfo=_RuckusL2TPInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,14,1,1,1))
class _RuckusL2TPServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_D,2)))
_RuckusL2TPServiceStatus_Type.__name__=_C
_RuckusL2TPServiceStatus_Object=MibScalar
ruckusL2TPServiceStatus=_RuckusL2TPServiceStatus_Object((1,3,6,1,4,1,25053,1,1,14,1,1,1,1),_RuckusL2TPServiceStatus_Type())
ruckusL2TPServiceStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusL2TPServiceStatus.setStatus(_B)
class _RuckusL2TPConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('connected',1),('disconnected',2),(_D,3)))
_RuckusL2TPConnectionStatus_Type.__name__=_C
_RuckusL2TPConnectionStatus_Object=MibScalar
ruckusL2TPConnectionStatus=_RuckusL2TPConnectionStatus_Object((1,3,6,1,4,1,25053,1,1,14,1,1,1,2),_RuckusL2TPConnectionStatus_Type())
ruckusL2TPConnectionStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusL2TPConnectionStatus.setStatus(_B)
_RuckusL2TPServerIP_Type=IpAddress
_RuckusL2TPServerIP_Object=MibScalar
ruckusL2TPServerIP=_RuckusL2TPServerIP_Object((1,3,6,1,4,1,25053,1,1,14,1,1,1,3),_RuckusL2TPServerIP_Type())
ruckusL2TPServerIP.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusL2TPServerIP.setStatus(_B)
_RuckusL2TPSharedSecret_Type=DisplayString
_RuckusL2TPSharedSecret_Object=MibScalar
ruckusL2TPSharedSecret=_RuckusL2TPSharedSecret_Object((1,3,6,1,4,1,25053,1,1,14,1,1,1,4),_RuckusL2TPSharedSecret_Type())
ruckusL2TPSharedSecret.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusL2TPSharedSecret.setStatus(_B)
_RuckusL2TPUserName_Type=DisplayString
_RuckusL2TPUserName_Object=MibScalar
ruckusL2TPUserName=_RuckusL2TPUserName_Object((1,3,6,1,4,1,25053,1,1,14,1,1,1,5),_RuckusL2TPUserName_Type())
ruckusL2TPUserName.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusL2TPUserName.setStatus(_B)
_RuckusL2TPPassword_Type=DisplayString
_RuckusL2TPPassword_Object=MibScalar
ruckusL2TPPassword=_RuckusL2TPPassword_Object((1,3,6,1,4,1,25053,1,1,14,1,1,1,6),_RuckusL2TPPassword_Type())
ruckusL2TPPassword.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusL2TPPassword.setStatus(_B)
_RuckusL2TPIfIPAddr_Type=IpAddress
_RuckusL2TPIfIPAddr_Object=MibScalar
ruckusL2TPIfIPAddr=_RuckusL2TPIfIPAddr_Object((1,3,6,1,4,1,25053,1,1,14,1,1,1,7),_RuckusL2TPIfIPAddr_Type())
ruckusL2TPIfIPAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusL2TPIfIPAddr.setStatus(_B)
_RuckusL2TPIfNetMask_Type=IpAddress
_RuckusL2TPIfNetMask_Object=MibScalar
ruckusL2TPIfNetMask=_RuckusL2TPIfNetMask_Object((1,3,6,1,4,1,25053,1,1,14,1,1,1,8),_RuckusL2TPIfNetMask_Type())
ruckusL2TPIfNetMask.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusL2TPIfNetMask.setStatus(_B)
_RuckusL2TPIfGateway_Type=IpAddress
_RuckusL2TPIfGateway_Object=MibScalar
ruckusL2TPIfGateway=_RuckusL2TPIfGateway_Object((1,3,6,1,4,1,25053,1,1,14,1,1,1,9),_RuckusL2TPIfGateway_Type())
ruckusL2TPIfGateway.setMaxAccess(_A)
if mibBuilder.loadTexts:ruckusL2TPIfGateway.setStatus(_B)
_RuckusL2TPEvents_ObjectIdentity=ObjectIdentity
ruckusL2TPEvents=_RuckusL2TPEvents_ObjectIdentity((1,3,6,1,4,1,25053,1,1,14,1,2))
mibBuilder.exportSymbols('RUCKUS-L2TP-MIB',**{'ruckusL2TPMIB':ruckusL2TPMIB,'ruckusL2TPObjects':ruckusL2TPObjects,'ruckusL2TPInfo':ruckusL2TPInfo,'ruckusL2TPServiceStatus':ruckusL2TPServiceStatus,'ruckusL2TPConnectionStatus':ruckusL2TPConnectionStatus,'ruckusL2TPServerIP':ruckusL2TPServerIP,'ruckusL2TPSharedSecret':ruckusL2TPSharedSecret,'ruckusL2TPUserName':ruckusL2TPUserName,'ruckusL2TPPassword':ruckusL2TPPassword,'ruckusL2TPIfIPAddr':ruckusL2TPIfIPAddr,'ruckusL2TPIfNetMask':ruckusL2TPIfNetMask,'ruckusL2TPIfGateway':ruckusL2TPIfGateway,'ruckusL2TPEvents':ruckusL2TPEvents})