_M='ciscoDot11CscConfigGlobalGroup'
_L='cDot11CscStateTransitions'
_K='cDot11CscRegistrationLifeTime'
_J='cDot11CscMnInactivityTime'
_I='cDot11CscOperMode'
_H='cDot11CscMnAuthenticatorAddress'
_G='cDot11CscRootNodeAddress'
_F='cDot11CscParentWdsAddress'
_E='cDot11CscAddressType'
_D='Integer32'
_C='read-only'
_B='CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval')
ciscoDot11CscMIB=ModuleIdentity((1,3,6,1,4,1,9,10,109))
if mibBuilder.loadTexts:ciscoDot11CscMIB.setRevisions(('2004-06-02 00:00','2003-05-06 00:00'))
_CiscoDot11CscMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11CscMIBObjects=_CiscoDot11CscMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,109,1))
_CiscoDot11CscConfigGlobal_ObjectIdentity=ObjectIdentity
ciscoDot11CscConfigGlobal=_CiscoDot11CscConfigGlobal_ObjectIdentity((1,3,6,1,4,1,9,10,109,1,1))
_CDot11CscAddressType_Type=InetAddressType
_CDot11CscAddressType_Object=MibScalar
cDot11CscAddressType=_CDot11CscAddressType_Object((1,3,6,1,4,1,9,10,109,1,1,1),_CDot11CscAddressType_Type())
cDot11CscAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CscAddressType.setStatus(_A)
_CDot11CscParentWdsAddress_Type=InetAddress
_CDot11CscParentWdsAddress_Object=MibScalar
cDot11CscParentWdsAddress=_CDot11CscParentWdsAddress_Object((1,3,6,1,4,1,9,10,109,1,1,2),_CDot11CscParentWdsAddress_Type())
cDot11CscParentWdsAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CscParentWdsAddress.setStatus(_A)
_CDot11CscRootNodeAddress_Type=InetAddress
_CDot11CscRootNodeAddress_Object=MibScalar
cDot11CscRootNodeAddress=_CDot11CscRootNodeAddress_Object((1,3,6,1,4,1,9,10,109,1,1,3),_CDot11CscRootNodeAddress_Type())
cDot11CscRootNodeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CscRootNodeAddress.setStatus(_A)
_CDot11CscMnAuthenticatorAddress_Type=InetAddress
_CDot11CscMnAuthenticatorAddress_Object=MibScalar
cDot11CscMnAuthenticatorAddress=_CDot11CscMnAuthenticatorAddress_Object((1,3,6,1,4,1,9,10,109,1,1,4),_CDot11CscMnAuthenticatorAddress_Type())
cDot11CscMnAuthenticatorAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CscMnAuthenticatorAddress.setStatus(_A)
class _CDot11CscOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('infrastructure',1),('distributed',2)))
_CDot11CscOperMode_Type.__name__=_D
_CDot11CscOperMode_Object=MibScalar
cDot11CscOperMode=_CDot11CscOperMode_Object((1,3,6,1,4,1,9,10,109,1,1,5),_CDot11CscOperMode_Type())
cDot11CscOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CscOperMode.setStatus(_A)
_CDot11CscMnInactivityTime_Type=TimeInterval
_CDot11CscMnInactivityTime_Object=MibScalar
cDot11CscMnInactivityTime=_CDot11CscMnInactivityTime_Object((1,3,6,1,4,1,9,10,109,1,1,6),_CDot11CscMnInactivityTime_Type())
cDot11CscMnInactivityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CscMnInactivityTime.setStatus(_A)
_CDot11CscRegistrationLifeTime_Type=TimeInterval
_CDot11CscRegistrationLifeTime_Object=MibScalar
cDot11CscRegistrationLifeTime=_CDot11CscRegistrationLifeTime_Object((1,3,6,1,4,1,9,10,109,1,1,7),_CDot11CscRegistrationLifeTime_Type())
cDot11CscRegistrationLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CscRegistrationLifeTime.setStatus(_A)
_CDot11CscStateTransitions_Type=Counter32
_CDot11CscStateTransitions_Object=MibScalar
cDot11CscStateTransitions=_CDot11CscStateTransitions_Object((1,3,6,1,4,1,9,10,109,1,1,8),_CDot11CscStateTransitions_Type())
cDot11CscStateTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11CscStateTransitions.setStatus(_A)
_CiscoDot11CscMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDot11CscMIBConformance=_CiscoDot11CscMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,109,2))
_CiscoDot11CscMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11CscMIBCompliances=_CiscoDot11CscMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,109,2,1))
_CiscoDot11CscMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11CscMIBGroups=_CiscoDot11CscMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,109,2,2))
ciscoDot11CscConfigGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,10,109,2,2,1))
ciscoDot11CscConfigGlobalGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ciscoDot11CscConfigGlobalGroup.setStatus(_A)
ciscoDot11CscMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,109,2,1,1))
ciscoDot11CscMIBCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:ciscoDot11CscMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDot11CscMIB':ciscoDot11CscMIB,'ciscoDot11CscMIBObjects':ciscoDot11CscMIBObjects,'ciscoDot11CscConfigGlobal':ciscoDot11CscConfigGlobal,_E:cDot11CscAddressType,_F:cDot11CscParentWdsAddress,_G:cDot11CscRootNodeAddress,_H:cDot11CscMnAuthenticatorAddress,_I:cDot11CscOperMode,_J:cDot11CscMnInactivityTime,_K:cDot11CscRegistrationLifeTime,_L:cDot11CscStateTransitions,'ciscoDot11CscMIBConformance':ciscoDot11CscMIBConformance,'ciscoDot11CscMIBCompliances':ciscoDot11CscMIBCompliances,'ciscoDot11CscMIBCompliance':ciscoDot11CscMIBCompliance,'ciscoDot11CscMIBGroups':ciscoDot11CscMIBGroups,_M:ciscoDot11CscConfigGlobalGroup})