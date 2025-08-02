_F='mwLogTransferTableIndex'
_E='not-accessible'
_D='mwSyslogTableIndex'
_C='MERU-SYSLOG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwDiagnostics,=mibBuilder.importSymbols('MERU-SMI','mwDiagnostics')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwSyslog=ModuleIdentity((1,3,6,1,4,1,15983,1,1,5,2))
_MwSyslogTable_Object=MibTable
mwSyslogTable=_MwSyslogTable_Object((1,3,6,1,4,1,15983,1,1,5,2,1))
if mibBuilder.loadTexts:mwSyslogTable.setStatus(_A)
_MwSyslogEntry_Object=MibTableRow
mwSyslogEntry=_MwSyslogEntry_Object((1,3,6,1,4,1,15983,1,1,5,2,1,1))
mwSyslogEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mwSyslogEntry.setStatus(_A)
_MwSyslogTableIndex_Type=Integer32
_MwSyslogTableIndex_Object=MibTableColumn
mwSyslogTableIndex=_MwSyslogTableIndex_Object((1,3,6,1,4,1,15983,1,1,5,2,1,1,1),_MwSyslogTableIndex_Type())
mwSyslogTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mwSyslogTableIndex.setStatus(_A)
_MwSysloglinenb_Type=Unsigned32
_MwSysloglinenb_Object=MibTableColumn
mwSysloglinenb=_MwSysloglinenb_Object((1,3,6,1,4,1,15983,1,1,5,2,1,1,2),_MwSysloglinenb_Type())
mwSysloglinenb.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSysloglinenb.setStatus(_A)
_MwSyslogrecord_Type=DisplayString
_MwSyslogrecord_Object=MibTableColumn
mwSyslogrecord=_MwSyslogrecord_Object((1,3,6,1,4,1,15983,1,1,5,2,1,1,3),_MwSyslogrecord_Type())
mwSyslogrecord.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSyslogrecord.setStatus(_A)
_MwSyslogpriority_Type=DisplayString
_MwSyslogpriority_Object=MibTableColumn
mwSyslogpriority=_MwSyslogpriority_Object((1,3,6,1,4,1,15983,1,1,5,2,1,1,4),_MwSyslogpriority_Type())
mwSyslogpriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSyslogpriority.setStatus(_A)
_MwSyslogmnemonic_Type=DisplayString
_MwSyslogmnemonic_Object=MibTableColumn
mwSyslogmnemonic=_MwSyslogmnemonic_Object((1,3,6,1,4,1,15983,1,1,5,2,1,1,5),_MwSyslogmnemonic_Type())
mwSyslogmnemonic.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSyslogmnemonic.setStatus(_A)
_MwSyslogtimestamp_Type=DateAndTime
_MwSyslogtimestamp_Object=MibTableColumn
mwSyslogtimestamp=_MwSyslogtimestamp_Object((1,3,6,1,4,1,15983,1,1,5,2,1,1,6),_MwSyslogtimestamp_Type())
mwSyslogtimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSyslogtimestamp.setStatus(_A)
_MwLogTransferTable_Object=MibTable
mwLogTransferTable=_MwLogTransferTable_Object((1,3,6,1,4,1,15983,1,1,5,2,2))
if mibBuilder.loadTexts:mwLogTransferTable.setStatus(_A)
_MwLogTransferEntry_Object=MibTableRow
mwLogTransferEntry=_MwLogTransferEntry_Object((1,3,6,1,4,1,15983,1,1,5,2,2,1))
mwLogTransferEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:mwLogTransferEntry.setStatus(_A)
_MwLogTransferTableIndex_Type=Integer32
_MwLogTransferTableIndex_Object=MibTableColumn
mwLogTransferTableIndex=_MwLogTransferTableIndex_Object((1,3,6,1,4,1,15983,1,1,5,2,2,1,1),_MwLogTransferTableIndex_Type())
mwLogTransferTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mwLogTransferTableIndex.setStatus(_A)
_MwLogTransfersize_Type=Unsigned32
_MwLogTransfersize_Object=MibTableColumn
mwLogTransfersize=_MwLogTransfersize_Object((1,3,6,1,4,1,15983,1,1,5,2,2,1,2),_MwLogTransfersize_Type())
mwLogTransfersize.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLogTransfersize.setStatus(_A)
_MwLogTransfernblines_Type=Unsigned32
_MwLogTransfernblines_Object=MibTableColumn
mwLogTransfernblines=_MwLogTransfernblines_Object((1,3,6,1,4,1,15983,1,1,5,2,2,1,3),_MwLogTransfernblines_Type())
mwLogTransfernblines.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLogTransfernblines.setStatus(_A)
_MwLogTransferlastaccess_Type=DateAndTime
_MwLogTransferlastaccess_Object=MibTableColumn
mwLogTransferlastaccess=_MwLogTransferlastaccess_Object((1,3,6,1,4,1,15983,1,1,5,2,2,1,4),_MwLogTransferlastaccess_Type())
mwLogTransferlastaccess.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLogTransferlastaccess.setStatus(_A)
_MwLogTransferlastrecord_Type=DisplayString
_MwLogTransferlastrecord_Object=MibTableColumn
mwLogTransferlastrecord=_MwLogTransferlastrecord_Object((1,3,6,1,4,1,15983,1,1,5,2,2,1,5),_MwLogTransferlastrecord_Type())
mwLogTransferlastrecord.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLogTransferlastrecord.setStatus(_A)
_MwLogTransferdescription_Type=DisplayString
_MwLogTransferdescription_Object=MibTableColumn
mwLogTransferdescription=_MwLogTransferdescription_Object((1,3,6,1,4,1,15983,1,1,5,2,2,1,6),_MwLogTransferdescription_Type())
mwLogTransferdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:mwLogTransferdescription.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mwSyslog':mwSyslog,'mwSyslogTable':mwSyslogTable,'mwSyslogEntry':mwSyslogEntry,_D:mwSyslogTableIndex,'mwSysloglinenb':mwSysloglinenb,'mwSyslogrecord':mwSyslogrecord,'mwSyslogpriority':mwSyslogpriority,'mwSyslogmnemonic':mwSyslogmnemonic,'mwSyslogtimestamp':mwSyslogtimestamp,'mwLogTransferTable':mwLogTransferTable,'mwLogTransferEntry':mwLogTransferEntry,_F:mwLogTransferTableIndex,'mwLogTransfersize':mwLogTransfersize,'mwLogTransfernblines':mwLogTransfernblines,'mwLogTransferlastaccess':mwLogTransferlastaccess,'mwLogTransferlastrecord':mwLogTransferlastrecord,'mwLogTransferdescription':mwLogTransferdescription})