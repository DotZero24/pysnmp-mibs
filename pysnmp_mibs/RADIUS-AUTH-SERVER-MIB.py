_w='radiusAuthServExtMIBGroup'
_v='radiusAuthServMIBGroup'
_u='radiusAuthServCounterDiscontinuity'
_t='radiusAuthServExtUnknownTypes'
_s='radiusAuthServExtPacketsDropped'
_r='radiusAuthServExtBadAuthenticators'
_q='radiusAuthServExtMalformedAccessRequests'
_p='radiusAuthServExtAccessChallenges'
_o='radiusAuthServExtAccessRejects'
_n='radiusAuthServExtAccessAccepts'
_m='radiusAuthServExtDupAccessRequests'
_l='radiusAuthServExtAccessRequests'
_k='radiusAuthClientExtID'
_j='radiusAuthClientInetAddress'
_i='radiusAuthClientInetAddressType'
_h='radiusAuthServUnknownTypes'
_g='radiusAuthServPacketsDropped'
_f='radiusAuthServBadAuthenticators'
_e='radiusAuthServMalformedAccessRequests'
_d='radiusAuthServAccessChallenges'
_c='radiusAuthServAccessRejects'
_b='radiusAuthServAccessAccepts'
_a='radiusAuthServDupAccessRequests'
_Z='radiusAuthServAccessRequests'
_Y='radiusAuthClientID'
_X='radiusAuthClientAddress'
_W='radiusAuthClientExtIndex'
_V='not-accessible'
_U='radiusAuthClientIndex'
_T='radiusAuthServTotalUnknownTypes'
_S='radiusAuthServTotalPacketsDropped'
_R='radiusAuthServTotalBadAuthenticators'
_Q='radiusAuthServTotalMalformedAccessRequests'
_P='radiusAuthServTotalAccessChallenges'
_O='radiusAuthServTotalAccessRejects'
_N='radiusAuthServTotalAccessAccepts'
_M='radiusAuthServTotalDupAccessRequests'
_L='radiusAuthServTotalInvalidRequests'
_K='radiusAuthServTotalAccessRequests'
_J='radiusAuthServConfigReset'
_I='radiusAuthServResetTime'
_H='radiusAuthServUpTime'
_G='radiusAuthServIdent'
_F='Integer32'
_E='deprecated'
_D='packets'
_C='current'
_B='read-only'
_A='RADIUS-AUTH-SERVER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
radiusAuthServMIB=ModuleIdentity((1,3,6,1,2,1,67,1,1))
if mibBuilder.loadTexts:radiusAuthServMIB.setRevisions(('2006-08-21 00:00','1999-06-11 00:00'))
_RadiusMIB_ObjectIdentity=ObjectIdentity
radiusMIB=_RadiusMIB_ObjectIdentity((1,3,6,1,2,1,67))
if mibBuilder.loadTexts:radiusMIB.setStatus(_C)
_RadiusAuthentication_ObjectIdentity=ObjectIdentity
radiusAuthentication=_RadiusAuthentication_ObjectIdentity((1,3,6,1,2,1,67,1))
_RadiusAuthServMIBObjects_ObjectIdentity=ObjectIdentity
radiusAuthServMIBObjects=_RadiusAuthServMIBObjects_ObjectIdentity((1,3,6,1,2,1,67,1,1,1))
_RadiusAuthServ_ObjectIdentity=ObjectIdentity
radiusAuthServ=_RadiusAuthServ_ObjectIdentity((1,3,6,1,2,1,67,1,1,1,1))
_RadiusAuthServIdent_Type=SnmpAdminString
_RadiusAuthServIdent_Object=MibScalar
radiusAuthServIdent=_RadiusAuthServIdent_Object((1,3,6,1,2,1,67,1,1,1,1,1),_RadiusAuthServIdent_Type())
radiusAuthServIdent.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServIdent.setStatus(_C)
_RadiusAuthServUpTime_Type=TimeTicks
_RadiusAuthServUpTime_Object=MibScalar
radiusAuthServUpTime=_RadiusAuthServUpTime_Object((1,3,6,1,2,1,67,1,1,1,1,2),_RadiusAuthServUpTime_Type())
radiusAuthServUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServUpTime.setStatus(_C)
_RadiusAuthServResetTime_Type=TimeTicks
_RadiusAuthServResetTime_Object=MibScalar
radiusAuthServResetTime=_RadiusAuthServResetTime_Object((1,3,6,1,2,1,67,1,1,1,1,3),_RadiusAuthServResetTime_Type())
radiusAuthServResetTime.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServResetTime.setStatus(_C)
class _RadiusAuthServConfigReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('reset',2),('initializing',3),('running',4)))
_RadiusAuthServConfigReset_Type.__name__=_F
_RadiusAuthServConfigReset_Object=MibScalar
radiusAuthServConfigReset=_RadiusAuthServConfigReset_Object((1,3,6,1,2,1,67,1,1,1,1,4),_RadiusAuthServConfigReset_Type())
radiusAuthServConfigReset.setMaxAccess('read-write')
if mibBuilder.loadTexts:radiusAuthServConfigReset.setStatus(_C)
_RadiusAuthServTotalAccessRequests_Type=Counter32
_RadiusAuthServTotalAccessRequests_Object=MibScalar
radiusAuthServTotalAccessRequests=_RadiusAuthServTotalAccessRequests_Object((1,3,6,1,2,1,67,1,1,1,1,5),_RadiusAuthServTotalAccessRequests_Type())
radiusAuthServTotalAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalAccessRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalAccessRequests.setUnits(_D)
_RadiusAuthServTotalInvalidRequests_Type=Counter32
_RadiusAuthServTotalInvalidRequests_Object=MibScalar
radiusAuthServTotalInvalidRequests=_RadiusAuthServTotalInvalidRequests_Object((1,3,6,1,2,1,67,1,1,1,1,6),_RadiusAuthServTotalInvalidRequests_Type())
radiusAuthServTotalInvalidRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalInvalidRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalInvalidRequests.setUnits(_D)
_RadiusAuthServTotalDupAccessRequests_Type=Counter32
_RadiusAuthServTotalDupAccessRequests_Object=MibScalar
radiusAuthServTotalDupAccessRequests=_RadiusAuthServTotalDupAccessRequests_Object((1,3,6,1,2,1,67,1,1,1,1,7),_RadiusAuthServTotalDupAccessRequests_Type())
radiusAuthServTotalDupAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalDupAccessRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalDupAccessRequests.setUnits(_D)
_RadiusAuthServTotalAccessAccepts_Type=Counter32
_RadiusAuthServTotalAccessAccepts_Object=MibScalar
radiusAuthServTotalAccessAccepts=_RadiusAuthServTotalAccessAccepts_Object((1,3,6,1,2,1,67,1,1,1,1,8),_RadiusAuthServTotalAccessAccepts_Type())
radiusAuthServTotalAccessAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalAccessAccepts.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalAccessAccepts.setUnits(_D)
_RadiusAuthServTotalAccessRejects_Type=Counter32
_RadiusAuthServTotalAccessRejects_Object=MibScalar
radiusAuthServTotalAccessRejects=_RadiusAuthServTotalAccessRejects_Object((1,3,6,1,2,1,67,1,1,1,1,9),_RadiusAuthServTotalAccessRejects_Type())
radiusAuthServTotalAccessRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalAccessRejects.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalAccessRejects.setUnits(_D)
_RadiusAuthServTotalAccessChallenges_Type=Counter32
_RadiusAuthServTotalAccessChallenges_Object=MibScalar
radiusAuthServTotalAccessChallenges=_RadiusAuthServTotalAccessChallenges_Object((1,3,6,1,2,1,67,1,1,1,1,10),_RadiusAuthServTotalAccessChallenges_Type())
radiusAuthServTotalAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalAccessChallenges.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalAccessChallenges.setUnits(_D)
_RadiusAuthServTotalMalformedAccessRequests_Type=Counter32
_RadiusAuthServTotalMalformedAccessRequests_Object=MibScalar
radiusAuthServTotalMalformedAccessRequests=_RadiusAuthServTotalMalformedAccessRequests_Object((1,3,6,1,2,1,67,1,1,1,1,11),_RadiusAuthServTotalMalformedAccessRequests_Type())
radiusAuthServTotalMalformedAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalMalformedAccessRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalMalformedAccessRequests.setUnits(_D)
_RadiusAuthServTotalBadAuthenticators_Type=Counter32
_RadiusAuthServTotalBadAuthenticators_Object=MibScalar
radiusAuthServTotalBadAuthenticators=_RadiusAuthServTotalBadAuthenticators_Object((1,3,6,1,2,1,67,1,1,1,1,12),_RadiusAuthServTotalBadAuthenticators_Type())
radiusAuthServTotalBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalBadAuthenticators.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalBadAuthenticators.setUnits(_D)
_RadiusAuthServTotalPacketsDropped_Type=Counter32
_RadiusAuthServTotalPacketsDropped_Object=MibScalar
radiusAuthServTotalPacketsDropped=_RadiusAuthServTotalPacketsDropped_Object((1,3,6,1,2,1,67,1,1,1,1,13),_RadiusAuthServTotalPacketsDropped_Type())
radiusAuthServTotalPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalPacketsDropped.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalPacketsDropped.setUnits(_D)
_RadiusAuthServTotalUnknownTypes_Type=Counter32
_RadiusAuthServTotalUnknownTypes_Object=MibScalar
radiusAuthServTotalUnknownTypes=_RadiusAuthServTotalUnknownTypes_Object((1,3,6,1,2,1,67,1,1,1,1,14),_RadiusAuthServTotalUnknownTypes_Type())
radiusAuthServTotalUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServTotalUnknownTypes.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServTotalUnknownTypes.setUnits(_D)
_RadiusAuthClientTable_Object=MibTable
radiusAuthClientTable=_RadiusAuthClientTable_Object((1,3,6,1,2,1,67,1,1,1,1,15))
if mibBuilder.loadTexts:radiusAuthClientTable.setStatus(_E)
_RadiusAuthClientEntry_Object=MibTableRow
radiusAuthClientEntry=_RadiusAuthClientEntry_Object((1,3,6,1,2,1,67,1,1,1,1,15,1))
radiusAuthClientEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:radiusAuthClientEntry.setStatus(_E)
class _RadiusAuthClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RadiusAuthClientIndex_Type.__name__=_F
_RadiusAuthClientIndex_Object=MibTableColumn
radiusAuthClientIndex=_RadiusAuthClientIndex_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,1),_RadiusAuthClientIndex_Type())
radiusAuthClientIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:radiusAuthClientIndex.setStatus(_E)
_RadiusAuthClientAddress_Type=IpAddress
_RadiusAuthClientAddress_Object=MibTableColumn
radiusAuthClientAddress=_RadiusAuthClientAddress_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,2),_RadiusAuthClientAddress_Type())
radiusAuthClientAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientAddress.setStatus(_E)
_RadiusAuthClientID_Type=SnmpAdminString
_RadiusAuthClientID_Object=MibTableColumn
radiusAuthClientID=_RadiusAuthClientID_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,3),_RadiusAuthClientID_Type())
radiusAuthClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientID.setStatus(_E)
_RadiusAuthServAccessRequests_Type=Counter32
_RadiusAuthServAccessRequests_Object=MibTableColumn
radiusAuthServAccessRequests=_RadiusAuthServAccessRequests_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,4),_RadiusAuthServAccessRequests_Type())
radiusAuthServAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServAccessRequests.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthServAccessRequests.setUnits(_D)
_RadiusAuthServDupAccessRequests_Type=Counter32
_RadiusAuthServDupAccessRequests_Object=MibTableColumn
radiusAuthServDupAccessRequests=_RadiusAuthServDupAccessRequests_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,5),_RadiusAuthServDupAccessRequests_Type())
radiusAuthServDupAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServDupAccessRequests.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthServDupAccessRequests.setUnits(_D)
_RadiusAuthServAccessAccepts_Type=Counter32
_RadiusAuthServAccessAccepts_Object=MibTableColumn
radiusAuthServAccessAccepts=_RadiusAuthServAccessAccepts_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,6),_RadiusAuthServAccessAccepts_Type())
radiusAuthServAccessAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServAccessAccepts.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthServAccessAccepts.setUnits(_D)
_RadiusAuthServAccessRejects_Type=Counter32
_RadiusAuthServAccessRejects_Object=MibTableColumn
radiusAuthServAccessRejects=_RadiusAuthServAccessRejects_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,7),_RadiusAuthServAccessRejects_Type())
radiusAuthServAccessRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServAccessRejects.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthServAccessRejects.setUnits(_D)
_RadiusAuthServAccessChallenges_Type=Counter32
_RadiusAuthServAccessChallenges_Object=MibTableColumn
radiusAuthServAccessChallenges=_RadiusAuthServAccessChallenges_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,8),_RadiusAuthServAccessChallenges_Type())
radiusAuthServAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServAccessChallenges.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthServAccessChallenges.setUnits(_D)
_RadiusAuthServMalformedAccessRequests_Type=Counter32
_RadiusAuthServMalformedAccessRequests_Object=MibTableColumn
radiusAuthServMalformedAccessRequests=_RadiusAuthServMalformedAccessRequests_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,9),_RadiusAuthServMalformedAccessRequests_Type())
radiusAuthServMalformedAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServMalformedAccessRequests.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthServMalformedAccessRequests.setUnits(_D)
_RadiusAuthServBadAuthenticators_Type=Counter32
_RadiusAuthServBadAuthenticators_Object=MibTableColumn
radiusAuthServBadAuthenticators=_RadiusAuthServBadAuthenticators_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,10),_RadiusAuthServBadAuthenticators_Type())
radiusAuthServBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServBadAuthenticators.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthServBadAuthenticators.setUnits(_D)
_RadiusAuthServPacketsDropped_Type=Counter32
_RadiusAuthServPacketsDropped_Object=MibTableColumn
radiusAuthServPacketsDropped=_RadiusAuthServPacketsDropped_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,11),_RadiusAuthServPacketsDropped_Type())
radiusAuthServPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServPacketsDropped.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthServPacketsDropped.setUnits(_D)
_RadiusAuthServUnknownTypes_Type=Counter32
_RadiusAuthServUnknownTypes_Object=MibTableColumn
radiusAuthServUnknownTypes=_RadiusAuthServUnknownTypes_Object((1,3,6,1,2,1,67,1,1,1,1,15,1,12),_RadiusAuthServUnknownTypes_Type())
radiusAuthServUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServUnknownTypes.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthServUnknownTypes.setUnits(_D)
_RadiusAuthClientExtTable_Object=MibTable
radiusAuthClientExtTable=_RadiusAuthClientExtTable_Object((1,3,6,1,2,1,67,1,1,1,1,16))
if mibBuilder.loadTexts:radiusAuthClientExtTable.setStatus(_C)
_RadiusAuthClientExtEntry_Object=MibTableRow
radiusAuthClientExtEntry=_RadiusAuthClientExtEntry_Object((1,3,6,1,2,1,67,1,1,1,1,16,1))
radiusAuthClientExtEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:radiusAuthClientExtEntry.setStatus(_C)
class _RadiusAuthClientExtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RadiusAuthClientExtIndex_Type.__name__=_F
_RadiusAuthClientExtIndex_Object=MibTableColumn
radiusAuthClientExtIndex=_RadiusAuthClientExtIndex_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,1),_RadiusAuthClientExtIndex_Type())
radiusAuthClientExtIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:radiusAuthClientExtIndex.setStatus(_C)
_RadiusAuthClientInetAddressType_Type=InetAddressType
_RadiusAuthClientInetAddressType_Object=MibTableColumn
radiusAuthClientInetAddressType=_RadiusAuthClientInetAddressType_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,2),_RadiusAuthClientInetAddressType_Type())
radiusAuthClientInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientInetAddressType.setStatus(_C)
_RadiusAuthClientInetAddress_Type=InetAddress
_RadiusAuthClientInetAddress_Object=MibTableColumn
radiusAuthClientInetAddress=_RadiusAuthClientInetAddress_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,3),_RadiusAuthClientInetAddress_Type())
radiusAuthClientInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientInetAddress.setStatus(_C)
_RadiusAuthClientExtID_Type=SnmpAdminString
_RadiusAuthClientExtID_Object=MibTableColumn
radiusAuthClientExtID=_RadiusAuthClientExtID_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,4),_RadiusAuthClientExtID_Type())
radiusAuthClientExtID.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtID.setStatus(_C)
_RadiusAuthServExtAccessRequests_Type=Counter32
_RadiusAuthServExtAccessRequests_Object=MibTableColumn
radiusAuthServExtAccessRequests=_RadiusAuthServExtAccessRequests_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,5),_RadiusAuthServExtAccessRequests_Type())
radiusAuthServExtAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServExtAccessRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServExtAccessRequests.setUnits(_D)
_RadiusAuthServExtDupAccessRequests_Type=Counter32
_RadiusAuthServExtDupAccessRequests_Object=MibTableColumn
radiusAuthServExtDupAccessRequests=_RadiusAuthServExtDupAccessRequests_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,6),_RadiusAuthServExtDupAccessRequests_Type())
radiusAuthServExtDupAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServExtDupAccessRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServExtDupAccessRequests.setUnits(_D)
_RadiusAuthServExtAccessAccepts_Type=Counter32
_RadiusAuthServExtAccessAccepts_Object=MibTableColumn
radiusAuthServExtAccessAccepts=_RadiusAuthServExtAccessAccepts_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,7),_RadiusAuthServExtAccessAccepts_Type())
radiusAuthServExtAccessAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServExtAccessAccepts.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServExtAccessAccepts.setUnits(_D)
_RadiusAuthServExtAccessRejects_Type=Counter32
_RadiusAuthServExtAccessRejects_Object=MibTableColumn
radiusAuthServExtAccessRejects=_RadiusAuthServExtAccessRejects_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,8),_RadiusAuthServExtAccessRejects_Type())
radiusAuthServExtAccessRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServExtAccessRejects.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServExtAccessRejects.setUnits(_D)
_RadiusAuthServExtAccessChallenges_Type=Counter32
_RadiusAuthServExtAccessChallenges_Object=MibTableColumn
radiusAuthServExtAccessChallenges=_RadiusAuthServExtAccessChallenges_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,9),_RadiusAuthServExtAccessChallenges_Type())
radiusAuthServExtAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServExtAccessChallenges.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServExtAccessChallenges.setUnits(_D)
_RadiusAuthServExtMalformedAccessRequests_Type=Counter32
_RadiusAuthServExtMalformedAccessRequests_Object=MibTableColumn
radiusAuthServExtMalformedAccessRequests=_RadiusAuthServExtMalformedAccessRequests_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,10),_RadiusAuthServExtMalformedAccessRequests_Type())
radiusAuthServExtMalformedAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServExtMalformedAccessRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServExtMalformedAccessRequests.setUnits(_D)
_RadiusAuthServExtBadAuthenticators_Type=Counter32
_RadiusAuthServExtBadAuthenticators_Object=MibTableColumn
radiusAuthServExtBadAuthenticators=_RadiusAuthServExtBadAuthenticators_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,11),_RadiusAuthServExtBadAuthenticators_Type())
radiusAuthServExtBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServExtBadAuthenticators.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServExtBadAuthenticators.setUnits(_D)
_RadiusAuthServExtPacketsDropped_Type=Counter32
_RadiusAuthServExtPacketsDropped_Object=MibTableColumn
radiusAuthServExtPacketsDropped=_RadiusAuthServExtPacketsDropped_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,12),_RadiusAuthServExtPacketsDropped_Type())
radiusAuthServExtPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServExtPacketsDropped.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServExtPacketsDropped.setUnits(_D)
_RadiusAuthServExtUnknownTypes_Type=Counter32
_RadiusAuthServExtUnknownTypes_Object=MibTableColumn
radiusAuthServExtUnknownTypes=_RadiusAuthServExtUnknownTypes_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,13),_RadiusAuthServExtUnknownTypes_Type())
radiusAuthServExtUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServExtUnknownTypes.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServExtUnknownTypes.setUnits(_D)
_RadiusAuthServCounterDiscontinuity_Type=TimeTicks
_RadiusAuthServCounterDiscontinuity_Object=MibTableColumn
radiusAuthServCounterDiscontinuity=_RadiusAuthServCounterDiscontinuity_Object((1,3,6,1,2,1,67,1,1,1,1,16,1,14),_RadiusAuthServCounterDiscontinuity_Type())
radiusAuthServCounterDiscontinuity.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServCounterDiscontinuity.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthServCounterDiscontinuity.setUnits('centiseconds')
_RadiusAuthServMIBConformance_ObjectIdentity=ObjectIdentity
radiusAuthServMIBConformance=_RadiusAuthServMIBConformance_ObjectIdentity((1,3,6,1,2,1,67,1,1,2))
_RadiusAuthServMIBCompliances_ObjectIdentity=ObjectIdentity
radiusAuthServMIBCompliances=_RadiusAuthServMIBCompliances_ObjectIdentity((1,3,6,1,2,1,67,1,1,2,1))
_RadiusAuthServMIBGroups_ObjectIdentity=ObjectIdentity
radiusAuthServMIBGroups=_RadiusAuthServMIBGroups_ObjectIdentity((1,3,6,1,2,1,67,1,1,2,2))
radiusAuthServMIBGroup=ObjectGroup((1,3,6,1,2,1,67,1,1,2,2,1))
radiusAuthServMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:radiusAuthServMIBGroup.setStatus(_E)
radiusAuthServExtMIBGroup=ObjectGroup((1,3,6,1,2,1,67,1,1,2,2,2))
radiusAuthServExtMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:radiusAuthServExtMIBGroup.setStatus(_C)
radiusAuthServMIBCompliance=ModuleCompliance((1,3,6,1,2,1,67,1,1,2,1,1))
radiusAuthServMIBCompliance.setObjects((_A,_v))
if mibBuilder.loadTexts:radiusAuthServMIBCompliance.setStatus(_E)
radiusAuthServMIBExtCompliance=ModuleCompliance((1,3,6,1,2,1,67,1,1,2,1,2))
radiusAuthServMIBExtCompliance.setObjects((_A,_w))
if mibBuilder.loadTexts:radiusAuthServMIBExtCompliance.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'radiusMIB':radiusMIB,'radiusAuthentication':radiusAuthentication,'radiusAuthServMIB':radiusAuthServMIB,'radiusAuthServMIBObjects':radiusAuthServMIBObjects,'radiusAuthServ':radiusAuthServ,_G:radiusAuthServIdent,_H:radiusAuthServUpTime,_I:radiusAuthServResetTime,_J:radiusAuthServConfigReset,_K:radiusAuthServTotalAccessRequests,_L:radiusAuthServTotalInvalidRequests,_M:radiusAuthServTotalDupAccessRequests,_N:radiusAuthServTotalAccessAccepts,_O:radiusAuthServTotalAccessRejects,_P:radiusAuthServTotalAccessChallenges,_Q:radiusAuthServTotalMalformedAccessRequests,_R:radiusAuthServTotalBadAuthenticators,_S:radiusAuthServTotalPacketsDropped,_T:radiusAuthServTotalUnknownTypes,'radiusAuthClientTable':radiusAuthClientTable,'radiusAuthClientEntry':radiusAuthClientEntry,_U:radiusAuthClientIndex,_X:radiusAuthClientAddress,_Y:radiusAuthClientID,_Z:radiusAuthServAccessRequests,_a:radiusAuthServDupAccessRequests,_b:radiusAuthServAccessAccepts,_c:radiusAuthServAccessRejects,_d:radiusAuthServAccessChallenges,_e:radiusAuthServMalformedAccessRequests,_f:radiusAuthServBadAuthenticators,_g:radiusAuthServPacketsDropped,_h:radiusAuthServUnknownTypes,'radiusAuthClientExtTable':radiusAuthClientExtTable,'radiusAuthClientExtEntry':radiusAuthClientExtEntry,_W:radiusAuthClientExtIndex,_i:radiusAuthClientInetAddressType,_j:radiusAuthClientInetAddress,_k:radiusAuthClientExtID,_l:radiusAuthServExtAccessRequests,_m:radiusAuthServExtDupAccessRequests,_n:radiusAuthServExtAccessAccepts,_o:radiusAuthServExtAccessRejects,_p:radiusAuthServExtAccessChallenges,_q:radiusAuthServExtMalformedAccessRequests,_r:radiusAuthServExtBadAuthenticators,_s:radiusAuthServExtPacketsDropped,_t:radiusAuthServExtUnknownTypes,_u:radiusAuthServCounterDiscontinuity,'radiusAuthServMIBConformance':radiusAuthServMIBConformance,'radiusAuthServMIBCompliances':radiusAuthServMIBCompliances,'radiusAuthServMIBCompliance':radiusAuthServMIBCompliance,'radiusAuthServMIBExtCompliance':radiusAuthServMIBExtCompliance,'radiusAuthServMIBGroups':radiusAuthServMIBGroups,_v:radiusAuthServMIBGroup,_w:radiusAuthServExtMIBGroup})