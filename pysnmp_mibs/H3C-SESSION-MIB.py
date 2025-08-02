_I='h3cSessionEntIndex'
_H='h3cSessionStatCPUID'
_G='h3cSessionStatSlot'
_F='h3cSessionStatChassis'
_E='not-accessible'
_D='H3C-SESSION-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cSession=ModuleIdentity((1,3,6,1,4,1,2011,10,2,149))
if mibBuilder.loadTexts:h3cSession.setRevisions(('2016-12-25 11:05','2014-10-14 18:30','2014-07-15 15:30','2013-12-20 00:00'))
_H3cSessionTables_ObjectIdentity=ObjectIdentity
h3cSessionTables=_H3cSessionTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,149,1))
_H3cSessionStatTable_Object=MibTable
h3cSessionStatTable=_H3cSessionStatTable_Object((1,3,6,1,4,1,2011,10,2,149,1,1))
if mibBuilder.loadTexts:h3cSessionStatTable.setStatus(_A)
_H3cSessionStatEntry_Object=MibTableRow
h3cSessionStatEntry=_H3cSessionStatEntry_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1))
h3cSessionStatEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:h3cSessionStatEntry.setStatus(_A)
class _H3cSessionStatChassis_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_H3cSessionStatChassis_Type.__name__=_C
_H3cSessionStatChassis_Object=MibTableColumn
h3cSessionStatChassis=_H3cSessionStatChassis_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,1),_H3cSessionStatChassis_Type())
h3cSessionStatChassis.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSessionStatChassis.setStatus(_A)
class _H3cSessionStatSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_H3cSessionStatSlot_Type.__name__=_C
_H3cSessionStatSlot_Object=MibTableColumn
h3cSessionStatSlot=_H3cSessionStatSlot_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,2),_H3cSessionStatSlot_Type())
h3cSessionStatSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSessionStatSlot.setStatus(_A)
class _H3cSessionStatCPUID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cSessionStatCPUID_Type.__name__=_C
_H3cSessionStatCPUID_Object=MibTableColumn
h3cSessionStatCPUID=_H3cSessionStatCPUID_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,3),_H3cSessionStatCPUID_Type())
h3cSessionStatCPUID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSessionStatCPUID.setStatus(_A)
_H3cSessionStatCount_Type=Unsigned32
_H3cSessionStatCount_Object=MibTableColumn
h3cSessionStatCount=_H3cSessionStatCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,4),_H3cSessionStatCount_Type())
h3cSessionStatCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatCount.setStatus(_A)
_H3cSessionStatCreateRate_Type=Unsigned32
_H3cSessionStatCreateRate_Object=MibTableColumn
h3cSessionStatCreateRate=_H3cSessionStatCreateRate_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,5),_H3cSessionStatCreateRate_Type())
h3cSessionStatCreateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatCreateRate.setStatus(_A)
_H3cSessionStatTCPCount_Type=Unsigned32
_H3cSessionStatTCPCount_Object=MibTableColumn
h3cSessionStatTCPCount=_H3cSessionStatTCPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,6),_H3cSessionStatTCPCount_Type())
h3cSessionStatTCPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatTCPCount.setStatus(_A)
_H3cSessionStatUDPCount_Type=Unsigned32
_H3cSessionStatUDPCount_Object=MibTableColumn
h3cSessionStatUDPCount=_H3cSessionStatUDPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,7),_H3cSessionStatUDPCount_Type())
h3cSessionStatUDPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatUDPCount.setStatus(_A)
_H3cSessionStatOtherCount_Type=Unsigned32
_H3cSessionStatOtherCount_Object=MibTableColumn
h3cSessionStatOtherCount=_H3cSessionStatOtherCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,8),_H3cSessionStatOtherCount_Type())
h3cSessionStatOtherCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatOtherCount.setStatus(_A)
_H3cSessionStatTCPCreateRate_Type=Unsigned32
_H3cSessionStatTCPCreateRate_Object=MibTableColumn
h3cSessionStatTCPCreateRate=_H3cSessionStatTCPCreateRate_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,9),_H3cSessionStatTCPCreateRate_Type())
h3cSessionStatTCPCreateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatTCPCreateRate.setStatus(_A)
_H3cSessionStatUDPCreateRate_Type=Unsigned32
_H3cSessionStatUDPCreateRate_Object=MibTableColumn
h3cSessionStatUDPCreateRate=_H3cSessionStatUDPCreateRate_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,10),_H3cSessionStatUDPCreateRate_Type())
h3cSessionStatUDPCreateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatUDPCreateRate.setStatus(_A)
_H3cSessionStatOtherCreateRate_Type=Unsigned32
_H3cSessionStatOtherCreateRate_Object=MibTableColumn
h3cSessionStatOtherCreateRate=_H3cSessionStatOtherCreateRate_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,11),_H3cSessionStatOtherCreateRate_Type())
h3cSessionStatOtherCreateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatOtherCreateRate.setStatus(_A)
_H3cSessionStatTCPTotal_Type=Counter64
_H3cSessionStatTCPTotal_Object=MibTableColumn
h3cSessionStatTCPTotal=_H3cSessionStatTCPTotal_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,12),_H3cSessionStatTCPTotal_Type())
h3cSessionStatTCPTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatTCPTotal.setStatus(_A)
_H3cSessionStatUDPTotal_Type=Counter64
_H3cSessionStatUDPTotal_Object=MibTableColumn
h3cSessionStatUDPTotal=_H3cSessionStatUDPTotal_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,13),_H3cSessionStatUDPTotal_Type())
h3cSessionStatUDPTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatUDPTotal.setStatus(_A)
_H3cSessionStatOtherTotal_Type=Counter64
_H3cSessionStatOtherTotal_Object=MibTableColumn
h3cSessionStatOtherTotal=_H3cSessionStatOtherTotal_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,14),_H3cSessionStatOtherTotal_Type())
h3cSessionStatOtherTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatOtherTotal.setStatus(_A)
_H3cSessionStatDNSCount_Type=Unsigned32
_H3cSessionStatDNSCount_Object=MibTableColumn
h3cSessionStatDNSCount=_H3cSessionStatDNSCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,15),_H3cSessionStatDNSCount_Type())
h3cSessionStatDNSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatDNSCount.setStatus(_A)
_H3cSessionStatFTPCount_Type=Unsigned32
_H3cSessionStatFTPCount_Object=MibTableColumn
h3cSessionStatFTPCount=_H3cSessionStatFTPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,16),_H3cSessionStatFTPCount_Type())
h3cSessionStatFTPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatFTPCount.setStatus(_A)
_H3cSessionStatGTPCount_Type=Unsigned32
_H3cSessionStatGTPCount_Object=MibTableColumn
h3cSessionStatGTPCount=_H3cSessionStatGTPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,17),_H3cSessionStatGTPCount_Type())
h3cSessionStatGTPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatGTPCount.setStatus(_A)
_H3cSessionStatH323Count_Type=Unsigned32
_H3cSessionStatH323Count_Object=MibTableColumn
h3cSessionStatH323Count=_H3cSessionStatH323Count_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,18),_H3cSessionStatH323Count_Type())
h3cSessionStatH323Count.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatH323Count.setStatus(_A)
_H3cSessionStatHTTPCount_Type=Unsigned32
_H3cSessionStatHTTPCount_Object=MibTableColumn
h3cSessionStatHTTPCount=_H3cSessionStatHTTPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,19),_H3cSessionStatHTTPCount_Type())
h3cSessionStatHTTPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatHTTPCount.setStatus(_A)
_H3cSessionStatILSCount_Type=Unsigned32
_H3cSessionStatILSCount_Object=MibTableColumn
h3cSessionStatILSCount=_H3cSessionStatILSCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,20),_H3cSessionStatILSCount_Type())
h3cSessionStatILSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatILSCount.setStatus(_A)
_H3cSessionStatMGCPCount_Type=Unsigned32
_H3cSessionStatMGCPCount_Object=MibTableColumn
h3cSessionStatMGCPCount=_H3cSessionStatMGCPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,21),_H3cSessionStatMGCPCount_Type())
h3cSessionStatMGCPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatMGCPCount.setStatus(_A)
_H3cSessionStatNBTCount_Type=Unsigned32
_H3cSessionStatNBTCount_Object=MibTableColumn
h3cSessionStatNBTCount=_H3cSessionStatNBTCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,22),_H3cSessionStatNBTCount_Type())
h3cSessionStatNBTCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatNBTCount.setStatus(_A)
_H3cSessionStatPPTPCount_Type=Unsigned32
_H3cSessionStatPPTPCount_Object=MibTableColumn
h3cSessionStatPPTPCount=_H3cSessionStatPPTPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,23),_H3cSessionStatPPTPCount_Type())
h3cSessionStatPPTPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatPPTPCount.setStatus(_A)
_H3cSessionStatRSHCount_Type=Unsigned32
_H3cSessionStatRSHCount_Object=MibTableColumn
h3cSessionStatRSHCount=_H3cSessionStatRSHCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,24),_H3cSessionStatRSHCount_Type())
h3cSessionStatRSHCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatRSHCount.setStatus(_A)
_H3cSessionStatRTSPCount_Type=Unsigned32
_H3cSessionStatRTSPCount_Object=MibTableColumn
h3cSessionStatRTSPCount=_H3cSessionStatRTSPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,25),_H3cSessionStatRTSPCount_Type())
h3cSessionStatRTSPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatRTSPCount.setStatus(_A)
_H3cSessionStatSCCPCount_Type=Unsigned32
_H3cSessionStatSCCPCount_Object=MibTableColumn
h3cSessionStatSCCPCount=_H3cSessionStatSCCPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,26),_H3cSessionStatSCCPCount_Type())
h3cSessionStatSCCPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatSCCPCount.setStatus(_A)
_H3cSessionStatSIPCount_Type=Unsigned32
_H3cSessionStatSIPCount_Object=MibTableColumn
h3cSessionStatSIPCount=_H3cSessionStatSIPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,27),_H3cSessionStatSIPCount_Type())
h3cSessionStatSIPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatSIPCount.setStatus(_A)
_H3cSessionStatSMTPCount_Type=Unsigned32
_H3cSessionStatSMTPCount_Object=MibTableColumn
h3cSessionStatSMTPCount=_H3cSessionStatSMTPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,28),_H3cSessionStatSMTPCount_Type())
h3cSessionStatSMTPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatSMTPCount.setStatus(_A)
_H3cSessionStatSQLNETCount_Type=Unsigned32
_H3cSessionStatSQLNETCount_Object=MibTableColumn
h3cSessionStatSQLNETCount=_H3cSessionStatSQLNETCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,29),_H3cSessionStatSQLNETCount_Type())
h3cSessionStatSQLNETCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatSQLNETCount.setStatus(_A)
_H3cSessionStatSSHCount_Type=Unsigned32
_H3cSessionStatSSHCount_Object=MibTableColumn
h3cSessionStatSSHCount=_H3cSessionStatSSHCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,30),_H3cSessionStatSSHCount_Type())
h3cSessionStatSSHCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatSSHCount.setStatus(_A)
_H3cSessionStatTELNETCount_Type=Unsigned32
_H3cSessionStatTELNETCount_Object=MibTableColumn
h3cSessionStatTELNETCount=_H3cSessionStatTELNETCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,31),_H3cSessionStatTELNETCount_Type())
h3cSessionStatTELNETCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatTELNETCount.setStatus(_A)
_H3cSessionStatTFTPCount_Type=Unsigned32
_H3cSessionStatTFTPCount_Object=MibTableColumn
h3cSessionStatTFTPCount=_H3cSessionStatTFTPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,32),_H3cSessionStatTFTPCount_Type())
h3cSessionStatTFTPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatTFTPCount.setStatus(_A)
_H3cSessionStatXDMCPCount_Type=Unsigned32
_H3cSessionStatXDMCPCount_Object=MibTableColumn
h3cSessionStatXDMCPCount=_H3cSessionStatXDMCPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,1,1,33),_H3cSessionStatXDMCPCount_Type())
h3cSessionStatXDMCPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionStatXDMCPCount.setStatus(_A)
_H3cSessionEntTable_Object=MibTable
h3cSessionEntTable=_H3cSessionEntTable_Object((1,3,6,1,4,1,2011,10,2,149,1,2))
if mibBuilder.loadTexts:h3cSessionEntTable.setStatus(_A)
_H3cSessionEntEntry_Object=MibTableRow
h3cSessionEntEntry=_H3cSessionEntEntry_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1))
h3cSessionEntEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:h3cSessionEntEntry.setStatus(_A)
class _H3cSessionEntIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cSessionEntIndex_Type.__name__=_C
_H3cSessionEntIndex_Object=MibTableColumn
h3cSessionEntIndex=_H3cSessionEntIndex_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,1),_H3cSessionEntIndex_Type())
h3cSessionEntIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSessionEntIndex.setStatus(_A)
_H3cSessionEntCount_Type=Unsigned32
_H3cSessionEntCount_Object=MibTableColumn
h3cSessionEntCount=_H3cSessionEntCount_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,2),_H3cSessionEntCount_Type())
h3cSessionEntCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntCount.setStatus(_A)
_H3cSessionEntCreateRate_Type=Unsigned32
_H3cSessionEntCreateRate_Object=MibTableColumn
h3cSessionEntCreateRate=_H3cSessionEntCreateRate_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,3),_H3cSessionEntCreateRate_Type())
h3cSessionEntCreateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntCreateRate.setStatus(_A)
_H3cSessionEntTCPCount_Type=Unsigned32
_H3cSessionEntTCPCount_Object=MibTableColumn
h3cSessionEntTCPCount=_H3cSessionEntTCPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,4),_H3cSessionEntTCPCount_Type())
h3cSessionEntTCPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntTCPCount.setStatus(_A)
_H3cSessionEntUDPCount_Type=Unsigned32
_H3cSessionEntUDPCount_Object=MibTableColumn
h3cSessionEntUDPCount=_H3cSessionEntUDPCount_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,5),_H3cSessionEntUDPCount_Type())
h3cSessionEntUDPCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntUDPCount.setStatus(_A)
_H3cSessionEntOtherCount_Type=Unsigned32
_H3cSessionEntOtherCount_Object=MibTableColumn
h3cSessionEntOtherCount=_H3cSessionEntOtherCount_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,6),_H3cSessionEntOtherCount_Type())
h3cSessionEntOtherCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntOtherCount.setStatus(_A)
_H3cSessionEntTCPCreateRate_Type=Unsigned32
_H3cSessionEntTCPCreateRate_Object=MibTableColumn
h3cSessionEntTCPCreateRate=_H3cSessionEntTCPCreateRate_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,7),_H3cSessionEntTCPCreateRate_Type())
h3cSessionEntTCPCreateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntTCPCreateRate.setStatus(_A)
_H3cSessionEntUDPCreateRate_Type=Unsigned32
_H3cSessionEntUDPCreateRate_Object=MibTableColumn
h3cSessionEntUDPCreateRate=_H3cSessionEntUDPCreateRate_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,8),_H3cSessionEntUDPCreateRate_Type())
h3cSessionEntUDPCreateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntUDPCreateRate.setStatus(_A)
_H3cSessionEntOtherCreateRate_Type=Unsigned32
_H3cSessionEntOtherCreateRate_Object=MibTableColumn
h3cSessionEntOtherCreateRate=_H3cSessionEntOtherCreateRate_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,9),_H3cSessionEntOtherCreateRate_Type())
h3cSessionEntOtherCreateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntOtherCreateRate.setStatus(_A)
_H3cSessionEntTCPTotal_Type=Counter64
_H3cSessionEntTCPTotal_Object=MibTableColumn
h3cSessionEntTCPTotal=_H3cSessionEntTCPTotal_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,10),_H3cSessionEntTCPTotal_Type())
h3cSessionEntTCPTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntTCPTotal.setStatus(_A)
_H3cSessionEntUDPTotal_Type=Counter64
_H3cSessionEntUDPTotal_Object=MibTableColumn
h3cSessionEntUDPTotal=_H3cSessionEntUDPTotal_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,11),_H3cSessionEntUDPTotal_Type())
h3cSessionEntUDPTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntUDPTotal.setStatus(_A)
_H3cSessionEntOtherTotal_Type=Counter64
_H3cSessionEntOtherTotal_Object=MibTableColumn
h3cSessionEntOtherTotal=_H3cSessionEntOtherTotal_Object((1,3,6,1,4,1,2011,10,2,149,1,2,1,12),_H3cSessionEntOtherTotal_Type())
h3cSessionEntOtherTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cSessionEntOtherTotal.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cSession':h3cSession,'h3cSessionTables':h3cSessionTables,'h3cSessionStatTable':h3cSessionStatTable,'h3cSessionStatEntry':h3cSessionStatEntry,_F:h3cSessionStatChassis,_G:h3cSessionStatSlot,_H:h3cSessionStatCPUID,'h3cSessionStatCount':h3cSessionStatCount,'h3cSessionStatCreateRate':h3cSessionStatCreateRate,'h3cSessionStatTCPCount':h3cSessionStatTCPCount,'h3cSessionStatUDPCount':h3cSessionStatUDPCount,'h3cSessionStatOtherCount':h3cSessionStatOtherCount,'h3cSessionStatTCPCreateRate':h3cSessionStatTCPCreateRate,'h3cSessionStatUDPCreateRate':h3cSessionStatUDPCreateRate,'h3cSessionStatOtherCreateRate':h3cSessionStatOtherCreateRate,'h3cSessionStatTCPTotal':h3cSessionStatTCPTotal,'h3cSessionStatUDPTotal':h3cSessionStatUDPTotal,'h3cSessionStatOtherTotal':h3cSessionStatOtherTotal,'h3cSessionStatDNSCount':h3cSessionStatDNSCount,'h3cSessionStatFTPCount':h3cSessionStatFTPCount,'h3cSessionStatGTPCount':h3cSessionStatGTPCount,'h3cSessionStatH323Count':h3cSessionStatH323Count,'h3cSessionStatHTTPCount':h3cSessionStatHTTPCount,'h3cSessionStatILSCount':h3cSessionStatILSCount,'h3cSessionStatMGCPCount':h3cSessionStatMGCPCount,'h3cSessionStatNBTCount':h3cSessionStatNBTCount,'h3cSessionStatPPTPCount':h3cSessionStatPPTPCount,'h3cSessionStatRSHCount':h3cSessionStatRSHCount,'h3cSessionStatRTSPCount':h3cSessionStatRTSPCount,'h3cSessionStatSCCPCount':h3cSessionStatSCCPCount,'h3cSessionStatSIPCount':h3cSessionStatSIPCount,'h3cSessionStatSMTPCount':h3cSessionStatSMTPCount,'h3cSessionStatSQLNETCount':h3cSessionStatSQLNETCount,'h3cSessionStatSSHCount':h3cSessionStatSSHCount,'h3cSessionStatTELNETCount':h3cSessionStatTELNETCount,'h3cSessionStatTFTPCount':h3cSessionStatTFTPCount,'h3cSessionStatXDMCPCount':h3cSessionStatXDMCPCount,'h3cSessionEntTable':h3cSessionEntTable,'h3cSessionEntEntry':h3cSessionEntEntry,_I:h3cSessionEntIndex,'h3cSessionEntCount':h3cSessionEntCount,'h3cSessionEntCreateRate':h3cSessionEntCreateRate,'h3cSessionEntTCPCount':h3cSessionEntTCPCount,'h3cSessionEntUDPCount':h3cSessionEntUDPCount,'h3cSessionEntOtherCount':h3cSessionEntOtherCount,'h3cSessionEntTCPCreateRate':h3cSessionEntTCPCreateRate,'h3cSessionEntUDPCreateRate':h3cSessionEntUDPCreateRate,'h3cSessionEntOtherCreateRate':h3cSessionEntOtherCreateRate,'h3cSessionEntTCPTotal':h3cSessionEntTCPTotal,'h3cSessionEntUDPTotal':h3cSessionEntUDPTotal,'h3cSessionEntOtherTotal':h3cSessionEntOtherTotal})