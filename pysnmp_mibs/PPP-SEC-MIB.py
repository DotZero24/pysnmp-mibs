_K='read-only'
_J='pppSecuritySecretsIdIndex'
_I='pppSecuritySecretsLink'
_H='invalid'
_G='pppSecurityConfigPreference'
_F='pppSecurityConfigLink'
_E='OctetString'
_D='PPP-SEC-MIB'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ppp,=mibBuilder.importSymbols('PPP-LCP-MIB','ppp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_PppSecurity_ObjectIdentity=ObjectIdentity
pppSecurity=_PppSecurity_ObjectIdentity((1,3,6,1,2,1,10,23,2))
_PppSecurityProtocols_ObjectIdentity=ObjectIdentity
pppSecurityProtocols=_PppSecurityProtocols_ObjectIdentity((1,3,6,1,2,1,10,23,2,1))
_PppSecurityPapProtocol_ObjectIdentity=ObjectIdentity
pppSecurityPapProtocol=_PppSecurityPapProtocol_ObjectIdentity((1,3,6,1,2,1,10,23,2,1,1))
_PppSecurityChapMD5Protocol_ObjectIdentity=ObjectIdentity
pppSecurityChapMD5Protocol=_PppSecurityChapMD5Protocol_ObjectIdentity((1,3,6,1,2,1,10,23,2,1,2))
_PppSecurityConfigTable_Object=MibTable
pppSecurityConfigTable=_PppSecurityConfigTable_Object((1,3,6,1,2,1,10,23,2,2))
if mibBuilder.loadTexts:pppSecurityConfigTable.setStatus(_A)
_PppSecurityConfigEntry_Object=MibTableRow
pppSecurityConfigEntry=_PppSecurityConfigEntry_Object((1,3,6,1,2,1,10,23,2,2,1))
pppSecurityConfigEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:pppSecurityConfigEntry.setStatus(_A)
class _PppSecurityConfigLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppSecurityConfigLink_Type.__name__=_C
_PppSecurityConfigLink_Object=MibTableColumn
pppSecurityConfigLink=_PppSecurityConfigLink_Object((1,3,6,1,2,1,10,23,2,2,1,1),_PppSecurityConfigLink_Type())
pppSecurityConfigLink.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecurityConfigLink.setStatus(_A)
class _PppSecurityConfigPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppSecurityConfigPreference_Type.__name__=_C
_PppSecurityConfigPreference_Object=MibTableColumn
pppSecurityConfigPreference=_PppSecurityConfigPreference_Object((1,3,6,1,2,1,10,23,2,2,1,2),_PppSecurityConfigPreference_Type())
pppSecurityConfigPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecurityConfigPreference.setStatus(_A)
_PppSecurityConfigProtocol_Type=ObjectIdentifier
_PppSecurityConfigProtocol_Object=MibTableColumn
pppSecurityConfigProtocol=_PppSecurityConfigProtocol_Object((1,3,6,1,2,1,10,23,2,2,1,3),_PppSecurityConfigProtocol_Type())
pppSecurityConfigProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecurityConfigProtocol.setStatus(_A)
class _PppSecurityConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('valid',2)))
_PppSecurityConfigStatus_Type.__name__=_C
_PppSecurityConfigStatus_Object=MibTableColumn
pppSecurityConfigStatus=_PppSecurityConfigStatus_Object((1,3,6,1,2,1,10,23,2,2,1,4),_PppSecurityConfigStatus_Type())
pppSecurityConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecurityConfigStatus.setStatus(_A)
_PppSecuritySecretsTable_Object=MibTable
pppSecuritySecretsTable=_PppSecuritySecretsTable_Object((1,3,6,1,2,1,10,23,2,3))
if mibBuilder.loadTexts:pppSecuritySecretsTable.setStatus(_A)
_PppSecuritySecretsEntry_Object=MibTableRow
pppSecuritySecretsEntry=_PppSecuritySecretsEntry_Object((1,3,6,1,2,1,10,23,2,3,1))
pppSecuritySecretsEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:pppSecuritySecretsEntry.setStatus(_A)
class _PppSecuritySecretsLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppSecuritySecretsLink_Type.__name__=_C
_PppSecuritySecretsLink_Object=MibTableColumn
pppSecuritySecretsLink=_PppSecuritySecretsLink_Object((1,3,6,1,2,1,10,23,2,3,1,1),_PppSecuritySecretsLink_Type())
pppSecuritySecretsLink.setMaxAccess(_K)
if mibBuilder.loadTexts:pppSecuritySecretsLink.setStatus(_A)
class _PppSecuritySecretsIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppSecuritySecretsIdIndex_Type.__name__=_C
_PppSecuritySecretsIdIndex_Object=MibTableColumn
pppSecuritySecretsIdIndex=_PppSecuritySecretsIdIndex_Object((1,3,6,1,2,1,10,23,2,3,1,2),_PppSecuritySecretsIdIndex_Type())
pppSecuritySecretsIdIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:pppSecuritySecretsIdIndex.setStatus(_A)
class _PppSecuritySecretsDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local-to-remote',1),('remote-to-local',2)))
_PppSecuritySecretsDirection_Type.__name__=_C
_PppSecuritySecretsDirection_Object=MibTableColumn
pppSecuritySecretsDirection=_PppSecuritySecretsDirection_Object((1,3,6,1,2,1,10,23,2,3,1,3),_PppSecuritySecretsDirection_Type())
pppSecuritySecretsDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecuritySecretsDirection.setStatus(_A)
_PppSecuritySecretsProtocol_Type=ObjectIdentifier
_PppSecuritySecretsProtocol_Object=MibTableColumn
pppSecuritySecretsProtocol=_PppSecuritySecretsProtocol_Object((1,3,6,1,2,1,10,23,2,3,1,4),_PppSecuritySecretsProtocol_Type())
pppSecuritySecretsProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecuritySecretsProtocol.setStatus(_A)
class _PppSecuritySecretsIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PppSecuritySecretsIdentity_Type.__name__=_E
_PppSecuritySecretsIdentity_Object=MibTableColumn
pppSecuritySecretsIdentity=_PppSecuritySecretsIdentity_Object((1,3,6,1,2,1,10,23,2,3,1,5),_PppSecuritySecretsIdentity_Type())
pppSecuritySecretsIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecuritySecretsIdentity.setStatus(_A)
class _PppSecuritySecretsSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PppSecuritySecretsSecret_Type.__name__=_E
_PppSecuritySecretsSecret_Object=MibTableColumn
pppSecuritySecretsSecret=_PppSecuritySecretsSecret_Object((1,3,6,1,2,1,10,23,2,3,1,6),_PppSecuritySecretsSecret_Type())
pppSecuritySecretsSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecuritySecretsSecret.setStatus(_A)
class _PppSecuritySecretsStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('valid',2)))
_PppSecuritySecretsStatus_Type.__name__=_C
_PppSecuritySecretsStatus_Object=MibTableColumn
pppSecuritySecretsStatus=_PppSecuritySecretsStatus_Object((1,3,6,1,2,1,10,23,2,3,1,7),_PppSecuritySecretsStatus_Type())
pppSecuritySecretsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecuritySecretsStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'pppSecurity':pppSecurity,'pppSecurityProtocols':pppSecurityProtocols,'pppSecurityPapProtocol':pppSecurityPapProtocol,'pppSecurityChapMD5Protocol':pppSecurityChapMD5Protocol,'pppSecurityConfigTable':pppSecurityConfigTable,'pppSecurityConfigEntry':pppSecurityConfigEntry,_F:pppSecurityConfigLink,_G:pppSecurityConfigPreference,'pppSecurityConfigProtocol':pppSecurityConfigProtocol,'pppSecurityConfigStatus':pppSecurityConfigStatus,'pppSecuritySecretsTable':pppSecuritySecretsTable,'pppSecuritySecretsEntry':pppSecuritySecretsEntry,_I:pppSecuritySecretsLink,_J:pppSecuritySecretsIdIndex,'pppSecuritySecretsDirection':pppSecuritySecretsDirection,'pppSecuritySecretsProtocol':pppSecuritySecretsProtocol,'pppSecuritySecretsIdentity':pppSecuritySecretsIdentity,'pppSecuritySecretsSecret':pppSecuritySecretsSecret,'pppSecuritySecretsStatus':pppSecuritySecretsStatus})