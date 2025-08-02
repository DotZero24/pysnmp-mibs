_D='MPKEEPALIVE-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mpKeepaliveMib=ModuleIdentity((1,3,6,1,4,1,5651,3,800))
_MpKeepaliveTable_Object=MibTable
mpKeepaliveTable=_MpKeepaliveTable_Object((1,3,6,1,4,1,5651,3,800,1))
if mibBuilder.loadTexts:mpKeepaliveTable.setStatus(_A)
_MpKeepaliveEntry_Object=MibTableRow
mpKeepaliveEntry=_MpKeepaliveEntry_Object((1,3,6,1,4,1,5651,3,800,1,1))
mpKeepaliveEntry.setIndexNames((0,_D,'mpIfNmae'))
if mibBuilder.loadTexts:mpKeepaliveEntry.setStatus(_A)
_MpKaIfNmae_Type=DisplayString
_MpKaIfNmae_Object=MibTableColumn
mpKaIfNmae=_MpKaIfNmae_Object((1,3,6,1,4,1,5651,3,800,1,1,1),_MpKaIfNmae_Type())
mpKaIfNmae.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:mpKaIfNmae.setStatus(_A)
class _MpKaTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_MpKaTimeout_Type.__name__=_B
_MpKaTimeout_Object=MibTableColumn
mpKaTimeout=_MpKaTimeout_Object((1,3,6,1,4,1,5651,3,800,1,1,2),_MpKaTimeout_Type())
mpKaTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mpKaTimeout.setStatus(_A)
class _MpKaRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_MpKaRetry_Type.__name__=_B
_MpKaRetry_Object=MibTableColumn
mpKaRetry=_MpKaRetry_Object((1,3,6,1,4,1,5651,3,800,1,1,3),_MpKaRetry_Type())
mpKaRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:mpKaRetry.setStatus(_A)
_MpKaGateway_Type=IpAddress
_MpKaGateway_Object=MibTableColumn
mpKaGateway=_MpKaGateway_Object((1,3,6,1,4,1,5651,3,800,1,1,4),_MpKaGateway_Type())
mpKaGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mpKaGateway.setStatus(_A)
_MpKaRowstatus_Type=RowStatus
_MpKaRowstatus_Object=MibTableColumn
mpKaRowstatus=_MpKaRowstatus_Object((1,3,6,1,4,1,5651,3,800,1,1,5),_MpKaRowstatus_Type())
mpKaRowstatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mpKaRowstatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mpKeepaliveMib':mpKeepaliveMib,'mpKeepaliveTable':mpKeepaliveTable,'mpKeepaliveEntry':mpKeepaliveEntry,'mpKaIfNmae':mpKaIfNmae,'mpKaTimeout':mpKaTimeout,'mpKaRetry':mpKaRetry,'mpKaGateway':mpKaGateway,'mpKaRowstatus':mpKaRowstatus})