_I='not-accessible'
_H='jnxRsvpSessionIndex'
_G='jnxRsvpSessionName'
_F='DisplayString'
_E='JUNIPER-RSVP-MIB'
_D='Unsigned32'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention','TimeStamp')
jnxRsvpMIB=ModuleIdentity((1,3,6,1,4,1,2636,3,30))
if mibBuilder.loadTexts:jnxRsvpMIB.setRevisions(('2007-06-28 09:30',))
_JnxRsvpOperation_ObjectIdentity=ObjectIdentity
jnxRsvpOperation=_JnxRsvpOperation_ObjectIdentity((1,3,6,1,4,1,2636,3,30,1))
_JnxRsvpSessionTable_Object=MibTable
jnxRsvpSessionTable=_JnxRsvpSessionTable_Object((1,3,6,1,4,1,2636,3,30,1,1))
if mibBuilder.loadTexts:jnxRsvpSessionTable.setStatus(_A)
_JnxRsvpSessionEntry_Object=MibTableRow
jnxRsvpSessionEntry=_JnxRsvpSessionEntry_Object((1,3,6,1,4,1,2636,3,30,1,1,1))
jnxRsvpSessionEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:jnxRsvpSessionEntry.setStatus(_A)
class _JnxRsvpSessionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JnxRsvpSessionName_Type.__name__=_F
_JnxRsvpSessionName_Object=MibTableColumn
jnxRsvpSessionName=_JnxRsvpSessionName_Object((1,3,6,1,4,1,2636,3,30,1,1,1,1),_JnxRsvpSessionName_Type())
jnxRsvpSessionName.setMaxAccess(_I)
if mibBuilder.loadTexts:jnxRsvpSessionName.setStatus(_A)
_JnxRsvpSessionIndex_Type=Unsigned32
_JnxRsvpSessionIndex_Object=MibTableColumn
jnxRsvpSessionIndex=_JnxRsvpSessionIndex_Object((1,3,6,1,4,1,2636,3,30,1,1,1,2),_JnxRsvpSessionIndex_Type())
jnxRsvpSessionIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:jnxRsvpSessionIndex.setStatus(_A)
class _JnxRsvpSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_JnxRsvpSessionState_Type.__name__=_C
_JnxRsvpSessionState_Object=MibTableColumn
jnxRsvpSessionState=_JnxRsvpSessionState_Object((1,3,6,1,4,1,2636,3,30,1,1,1,3),_JnxRsvpSessionState_Type())
jnxRsvpSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionState.setStatus(_A)
_JnxRsvpSessionFrom_Type=IpAddress
_JnxRsvpSessionFrom_Object=MibTableColumn
jnxRsvpSessionFrom=_JnxRsvpSessionFrom_Object((1,3,6,1,4,1,2636,3,30,1,1,1,4),_JnxRsvpSessionFrom_Type())
jnxRsvpSessionFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionFrom.setStatus(_A)
_JnxRsvpSessionTo_Type=IpAddress
_JnxRsvpSessionTo_Object=MibTableColumn
jnxRsvpSessionTo=_JnxRsvpSessionTo_Object((1,3,6,1,4,1,2636,3,30,1,1,1,5),_JnxRsvpSessionTo_Type())
jnxRsvpSessionTo.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionTo.setStatus(_A)
class _JnxRsvpSessionLspId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JnxRsvpSessionLspId_Type.__name__=_D
_JnxRsvpSessionLspId_Object=MibTableColumn
jnxRsvpSessionLspId=_JnxRsvpSessionLspId_Object((1,3,6,1,4,1,2636,3,30,1,1,1,6),_JnxRsvpSessionLspId_Type())
jnxRsvpSessionLspId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionLspId.setStatus(_A)
class _JnxRsvpSessionTunnelId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JnxRsvpSessionTunnelId_Type.__name__=_D
_JnxRsvpSessionTunnelId_Object=MibTableColumn
jnxRsvpSessionTunnelId=_JnxRsvpSessionTunnelId_Object((1,3,6,1,4,1,2636,3,30,1,1,1,7),_JnxRsvpSessionTunnelId_Type())
jnxRsvpSessionTunnelId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionTunnelId.setStatus(_A)
class _JnxRsvpSessionPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('unknown',3)))
_JnxRsvpSessionPathType_Type.__name__=_C
_JnxRsvpSessionPathType_Object=MibTableColumn
jnxRsvpSessionPathType=_JnxRsvpSessionPathType_Object((1,3,6,1,4,1,2636,3,30,1,1,1,8),_JnxRsvpSessionPathType_Type())
jnxRsvpSessionPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionPathType.setStatus(_A)
class _JnxRsvpSessionRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ingress',1),('transit',2),('egress',3)))
_JnxRsvpSessionRole_Type.__name__=_C
_JnxRsvpSessionRole_Object=MibTableColumn
jnxRsvpSessionRole=_JnxRsvpSessionRole_Object((1,3,6,1,4,1,2636,3,30,1,1,1,9),_JnxRsvpSessionRole_Type())
jnxRsvpSessionRole.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionRole.setStatus(_A)
_JnxRsvpSessionDiscontinuityTime_Type=TimeStamp
_JnxRsvpSessionDiscontinuityTime_Object=MibTableColumn
jnxRsvpSessionDiscontinuityTime=_JnxRsvpSessionDiscontinuityTime_Object((1,3,6,1,4,1,2636,3,30,1,1,1,10),_JnxRsvpSessionDiscontinuityTime_Type())
jnxRsvpSessionDiscontinuityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionDiscontinuityTime.setStatus(_A)
_JnxRsvpSessionMplsOctets_Type=Counter64
_JnxRsvpSessionMplsOctets_Object=MibTableColumn
jnxRsvpSessionMplsOctets=_JnxRsvpSessionMplsOctets_Object((1,3,6,1,4,1,2636,3,30,1,1,1,11),_JnxRsvpSessionMplsOctets_Type())
jnxRsvpSessionMplsOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionMplsOctets.setStatus(_A)
_JnxRsvpSessionMplsPackets_Type=Counter64
_JnxRsvpSessionMplsPackets_Object=MibTableColumn
jnxRsvpSessionMplsPackets=_JnxRsvpSessionMplsPackets_Object((1,3,6,1,4,1,2636,3,30,1,1,1,12),_JnxRsvpSessionMplsPackets_Type())
jnxRsvpSessionMplsPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxRsvpSessionMplsPackets.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'jnxRsvpMIB':jnxRsvpMIB,'jnxRsvpOperation':jnxRsvpOperation,'jnxRsvpSessionTable':jnxRsvpSessionTable,'jnxRsvpSessionEntry':jnxRsvpSessionEntry,_G:jnxRsvpSessionName,_H:jnxRsvpSessionIndex,'jnxRsvpSessionState':jnxRsvpSessionState,'jnxRsvpSessionFrom':jnxRsvpSessionFrom,'jnxRsvpSessionTo':jnxRsvpSessionTo,'jnxRsvpSessionLspId':jnxRsvpSessionLspId,'jnxRsvpSessionTunnelId':jnxRsvpSessionTunnelId,'jnxRsvpSessionPathType':jnxRsvpSessionPathType,'jnxRsvpSessionRole':jnxRsvpSessionRole,'jnxRsvpSessionDiscontinuityTime':jnxRsvpSessionDiscontinuityTime,'jnxRsvpSessionMplsOctets':jnxRsvpSessionMplsOctets,'jnxRsvpSessionMplsPackets':jnxRsvpSessionMplsPackets})