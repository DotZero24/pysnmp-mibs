_F='read-create'
_E='dcxNTPServerIp'
_D='ARRIS-C3-NTP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmtsC3,=mibBuilder.importSymbols('ARRIS-MIB','cmtsC3')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
cmtsC3NTPMIB=ModuleIdentity((1,3,6,1,4,1,4115,1,4,3,7))
_DcxNTPObjects_ObjectIdentity=ObjectIdentity
dcxNTPObjects=_DcxNTPObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,7,1))
_DcxNTPServerTable_Object=MibTable
dcxNTPServerTable=_DcxNTPServerTable_Object((1,3,6,1,4,1,4115,1,4,3,7,1,1))
if mibBuilder.loadTexts:dcxNTPServerTable.setStatus(_A)
_DcxNTPServerEntry_Object=MibTableRow
dcxNTPServerEntry=_DcxNTPServerEntry_Object((1,3,6,1,4,1,4115,1,4,3,7,1,1,1))
dcxNTPServerEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dcxNTPServerEntry.setStatus(_A)
_DcxNTPServerIp_Type=IpAddress
_DcxNTPServerIp_Object=MibTableColumn
dcxNTPServerIp=_DcxNTPServerIp_Object((1,3,6,1,4,1,4115,1,4,3,7,1,1,1,1),_DcxNTPServerIp_Type())
dcxNTPServerIp.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dcxNTPServerIp.setStatus(_A)
class _DcxNTPServerInterval_Type(Integer32):defaultValue=300
_DcxNTPServerInterval_Type.__name__=_C
_DcxNTPServerInterval_Object=MibTableColumn
dcxNTPServerInterval=_DcxNTPServerInterval_Object((1,3,6,1,4,1,4115,1,4,3,7,1,1,1,2),_DcxNTPServerInterval_Type())
dcxNTPServerInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:dcxNTPServerInterval.setStatus(_A)
_DcxNTPServerSuccess_Type=Counter32
_DcxNTPServerSuccess_Object=MibTableColumn
dcxNTPServerSuccess=_DcxNTPServerSuccess_Object((1,3,6,1,4,1,4115,1,4,3,7,1,1,1,3),_DcxNTPServerSuccess_Type())
dcxNTPServerSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxNTPServerSuccess.setStatus(_A)
_DcxNTPServerAttempts_Type=Counter32
_DcxNTPServerAttempts_Object=MibTableColumn
dcxNTPServerAttempts=_DcxNTPServerAttempts_Object((1,3,6,1,4,1,4115,1,4,3,7,1,1,1,4),_DcxNTPServerAttempts_Type())
dcxNTPServerAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxNTPServerAttempts.setStatus(_A)
_DcxNTPServerOffset_Type=Integer32
_DcxNTPServerOffset_Object=MibTableColumn
dcxNTPServerOffset=_DcxNTPServerOffset_Object((1,3,6,1,4,1,4115,1,4,3,7,1,1,1,5),_DcxNTPServerOffset_Type())
dcxNTPServerOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxNTPServerOffset.setStatus(_A)
_DcxNTPServerStatus_Type=RowStatus
_DcxNTPServerStatus_Object=MibTableColumn
dcxNTPServerStatus=_DcxNTPServerStatus_Object((1,3,6,1,4,1,4115,1,4,3,7,1,1,1,6),_DcxNTPServerStatus_Type())
dcxNTPServerStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:dcxNTPServerStatus.setStatus(_A)
_DcxNTPMasterServer_Type=IpAddress
_DcxNTPMasterServer_Object=MibScalar
dcxNTPMasterServer=_DcxNTPMasterServer_Object((1,3,6,1,4,1,4115,1,4,3,7,1,2),_DcxNTPMasterServer_Type())
dcxNTPMasterServer.setMaxAccess('read-write')
if mibBuilder.loadTexts:dcxNTPMasterServer.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cmtsC3NTPMIB':cmtsC3NTPMIB,'dcxNTPObjects':dcxNTPObjects,'dcxNTPServerTable':dcxNTPServerTable,'dcxNTPServerEntry':dcxNTPServerEntry,_E:dcxNTPServerIp,'dcxNTPServerInterval':dcxNTPServerInterval,'dcxNTPServerSuccess':dcxNTPServerSuccess,'dcxNTPServerAttempts':dcxNTPServerAttempts,'dcxNTPServerOffset':dcxNTPServerOffset,'dcxNTPServerStatus':dcxNTPServerStatus,'dcxNTPMasterServer':dcxNTPMasterServer})