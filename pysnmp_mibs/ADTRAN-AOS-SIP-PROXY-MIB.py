_N='adSipProxyNotificationGroup'
_M='adSipProxyNotificationUtilityGroup'
_L='adSipProxyRollover'
_K='sysName'
_J='SNMPv2-MIB'
_I='adProxyRolloverCause'
_H='adProxyRolloverToServerInetAddress'
_G='adProxyRolloverToServerInetAddressType'
_F='adProxyRolloverFromServerInetAddress'
_E='adProxyRolloverFromServerInetAddressType'
_D='adProxyTimestamp'
_C='accessible-for-notify'
_B='current'
_A='ADTRAN-AOS-SIP-PROXY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOSConformance,adGenAOSVoice=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOSConformance','adGenAOSVoice')
adIdentityShared,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentityShared')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAOSSipProxy=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,5,5))
if mibBuilder.loadTexts:adGenAOSSipProxy.setRevisions(('2013-05-16 00:00',))
class AdProxyRolloverCauseTC(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transactionFailed',1),('pollFailed',2),('pollSucceeded',3)))
_AdSipProxy_ObjectIdentity=ObjectIdentity
adSipProxy=_AdSipProxy_ObjectIdentity((1,3,6,1,4,1,664,5,53,5,5))
_AdSipProxyTraps_ObjectIdentity=ObjectIdentity
adSipProxyTraps=_AdSipProxyTraps_ObjectIdentity((1,3,6,1,4,1,664,5,53,5,5,0))
_AdProxyTimestamp_Type=TimeTicks
_AdProxyTimestamp_Object=MibScalar
adProxyTimestamp=_AdProxyTimestamp_Object((1,3,6,1,4,1,664,5,53,5,5,1),_AdProxyTimestamp_Type())
adProxyTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:adProxyTimestamp.setStatus(_B)
_AdProxyRolloverFromServerInetAddressType_Type=InetAddressType
_AdProxyRolloverFromServerInetAddressType_Object=MibScalar
adProxyRolloverFromServerInetAddressType=_AdProxyRolloverFromServerInetAddressType_Object((1,3,6,1,4,1,664,5,53,5,5,2),_AdProxyRolloverFromServerInetAddressType_Type())
adProxyRolloverFromServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:adProxyRolloverFromServerInetAddressType.setStatus(_B)
_AdProxyRolloverFromServerInetAddress_Type=InetAddress
_AdProxyRolloverFromServerInetAddress_Object=MibScalar
adProxyRolloverFromServerInetAddress=_AdProxyRolloverFromServerInetAddress_Object((1,3,6,1,4,1,664,5,53,5,5,3),_AdProxyRolloverFromServerInetAddress_Type())
adProxyRolloverFromServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adProxyRolloverFromServerInetAddress.setStatus(_B)
_AdProxyRolloverToServerInetAddressType_Type=InetAddressType
_AdProxyRolloverToServerInetAddressType_Object=MibScalar
adProxyRolloverToServerInetAddressType=_AdProxyRolloverToServerInetAddressType_Object((1,3,6,1,4,1,664,5,53,5,5,4),_AdProxyRolloverToServerInetAddressType_Type())
adProxyRolloverToServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:adProxyRolloverToServerInetAddressType.setStatus(_B)
_AdProxyRolloverToServerInetAddress_Type=InetAddress
_AdProxyRolloverToServerInetAddress_Object=MibScalar
adProxyRolloverToServerInetAddress=_AdProxyRolloverToServerInetAddress_Object((1,3,6,1,4,1,664,5,53,5,5,5),_AdProxyRolloverToServerInetAddress_Type())
adProxyRolloverToServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adProxyRolloverToServerInetAddress.setStatus(_B)
_AdProxyRolloverCause_Type=AdProxyRolloverCauseTC
_AdProxyRolloverCause_Object=MibScalar
adProxyRolloverCause=_AdProxyRolloverCause_Object((1,3,6,1,4,1,664,5,53,5,5,6),_AdProxyRolloverCause_Type())
adProxyRolloverCause.setMaxAccess(_C)
if mibBuilder.loadTexts:adProxyRolloverCause.setStatus(_B)
_AdSipProxyConformance_ObjectIdentity=ObjectIdentity
adSipProxyConformance=_AdSipProxyConformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,14))
_AdSipProxyGroups_ObjectIdentity=ObjectIdentity
adSipProxyGroups=_AdSipProxyGroups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,14,1))
_AdSipProxyCompliances_ObjectIdentity=ObjectIdentity
adSipProxyCompliances=_AdSipProxyCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,14,2))
adSipProxyNotificationUtilityGroup=ObjectGroup((1,3,6,1,4,1,664,5,53,99,14,1,2))
adSipProxyNotificationUtilityGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:adSipProxyNotificationUtilityGroup.setStatus(_B)
adSipProxyRollover=NotificationType((1,3,6,1,4,1,664,5,53,5,5,0,1))
adSipProxyRollover.setObjects(*((_J,_K),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:adSipProxyRollover.setStatus(_B)
adSipProxyNotificationGroup=NotificationGroup((1,3,6,1,4,1,664,5,53,99,14,1,1))
adSipProxyNotificationGroup.setObjects((_A,_L))
if mibBuilder.loadTexts:adSipProxyNotificationGroup.setStatus(_B)
adSipProxyFullCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,14,2,1))
adSipProxyFullCompliance.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:adSipProxyFullCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'AdProxyRolloverCauseTC':AdProxyRolloverCauseTC,'adSipProxy':adSipProxy,'adSipProxyTraps':adSipProxyTraps,_L:adSipProxyRollover,_D:adProxyTimestamp,_E:adProxyRolloverFromServerInetAddressType,_F:adProxyRolloverFromServerInetAddress,_G:adProxyRolloverToServerInetAddressType,_H:adProxyRolloverToServerInetAddress,_I:adProxyRolloverCause,'adSipProxyConformance':adSipProxyConformance,'adSipProxyGroups':adSipProxyGroups,_N:adSipProxyNotificationGroup,_M:adSipProxyNotificationUtilityGroup,'adSipProxyCompliances':adSipProxyCompliances,'adSipProxyFullCompliance':adSipProxyFullCompliance,'adGenAOSSipProxy':adGenAOSSipProxy})