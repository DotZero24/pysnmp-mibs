_F='read-only'
_E='DisplayString'
_D='OctetString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ruckusCommonPPPOEModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonPPPOEModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ruckusPPPOEMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,8,1))
_RuckusPPPOEObjects_ObjectIdentity=ObjectIdentity
ruckusPPPOEObjects=_RuckusPPPOEObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,8,1,1))
_RuckusPPPOEInfo_ObjectIdentity=ObjectIdentity
ruckusPPPOEInfo=_RuckusPPPOEInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,8,1,1,1))
class _RuckusPPPOEUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusPPPOEUserName_Type.__name__=_E
_RuckusPPPOEUserName_Object=MibScalar
ruckusPPPOEUserName=_RuckusPPPOEUserName_Object((1,3,6,1,4,1,25053,1,1,8,1,1,1,1),_RuckusPPPOEUserName_Type())
ruckusPPPOEUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusPPPOEUserName.setStatus(_A)
class _RuckusPPPOEPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusPPPOEPassword_Type.__name__=_D
_RuckusPPPOEPassword_Object=MibScalar
ruckusPPPOEPassword=_RuckusPPPOEPassword_Object((1,3,6,1,4,1,25053,1,1,8,1,1,1,2),_RuckusPPPOEPassword_Type())
ruckusPPPOEPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusPPPOEPassword.setStatus(_A)
class _RuckusPPPOEConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('notConnected',2)))
_RuckusPPPOEConnectionStatus_Type.__name__=_B
_RuckusPPPOEConnectionStatus_Object=MibScalar
ruckusPPPOEConnectionStatus=_RuckusPPPOEConnectionStatus_Object((1,3,6,1,4,1,25053,1,1,8,1,1,1,3),_RuckusPPPOEConnectionStatus_Type())
ruckusPPPOEConnectionStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusPPPOEConnectionStatus.setStatus(_A)
class _RuckusPPPOEConnection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('connect',1),('disConnect',2),('ok',3),('disabled',4)))
_RuckusPPPOEConnection_Type.__name__=_B
_RuckusPPPOEConnection_Object=MibScalar
ruckusPPPOEConnection=_RuckusPPPOEConnection_Object((1,3,6,1,4,1,25053,1,1,8,1,1,1,4),_RuckusPPPOEConnection_Type())
ruckusPPPOEConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusPPPOEConnection.setStatus(_A)
_RuckusPPPOEIfindex_Type=InterfaceIndex
_RuckusPPPOEIfindex_Object=MibScalar
ruckusPPPOEIfindex=_RuckusPPPOEIfindex_Object((1,3,6,1,4,1,25053,1,1,8,1,1,1,5),_RuckusPPPOEIfindex_Type())
ruckusPPPOEIfindex.setMaxAccess(_F)
if mibBuilder.loadTexts:ruckusPPPOEIfindex.setStatus(_A)
class _RuckusPPPOEApply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('apply',1))
_RuckusPPPOEApply_Type.__name__=_B
_RuckusPPPOEApply_Object=MibScalar
ruckusPPPOEApply=_RuckusPPPOEApply_Object((1,3,6,1,4,1,25053,1,1,8,1,1,1,6),_RuckusPPPOEApply_Type())
ruckusPPPOEApply.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusPPPOEApply.setStatus(_A)
_RuckusPPPOEEvents_ObjectIdentity=ObjectIdentity
ruckusPPPOEEvents=_RuckusPPPOEEvents_ObjectIdentity((1,3,6,1,4,1,25053,1,1,8,1,2))
mibBuilder.exportSymbols('RUCKUS-PPPOE-MIB',**{'ruckusPPPOEMIB':ruckusPPPOEMIB,'ruckusPPPOEObjects':ruckusPPPOEObjects,'ruckusPPPOEInfo':ruckusPPPOEInfo,'ruckusPPPOEUserName':ruckusPPPOEUserName,'ruckusPPPOEPassword':ruckusPPPOEPassword,'ruckusPPPOEConnectionStatus':ruckusPPPOEConnectionStatus,'ruckusPPPOEConnection':ruckusPPPOEConnection,'ruckusPPPOEIfindex':ruckusPPPOEIfindex,'ruckusPPPOEApply':ruckusPPPOEApply,'ruckusPPPOEEvents':ruckusPPPOEEvents})