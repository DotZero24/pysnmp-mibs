_E='not-accessible'
_D='volIndex'
_C='NIMBLE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
nimble=ModuleIdentity((1,3,6,1,4,1,37447))
if mibBuilder.loadTexts:nimble.setRevisions(('2012-08-31 00:00','2012-06-12 00:00','2011-02-28 00:00'))
_Variables_ObjectIdentity=ObjectIdentity
variables=_Variables_ObjectIdentity((1,3,6,1,4,1,37447,1))
_VolNumberOfVolumes_Type=Unsigned32
_VolNumberOfVolumes_Object=MibScalar
volNumberOfVolumes=_VolNumberOfVolumes_Object((1,3,6,1,4,1,37447,1,1),_VolNumberOfVolumes_Type())
volNumberOfVolumes.setMaxAccess(_B)
if mibBuilder.loadTexts:volNumberOfVolumes.setStatus('obsolete')
_VolTable_Object=MibTable
volTable=_VolTable_Object((1,3,6,1,4,1,37447,1,2))
if mibBuilder.loadTexts:volTable.setStatus(_A)
_VolEntry_Object=MibTableRow
volEntry=_VolEntry_Object((1,3,6,1,4,1,37447,1,2,1))
volEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:volEntry.setStatus(_A)
_VolIndex_Type=Unsigned32
_VolIndex_Object=MibTableColumn
volIndex=_VolIndex_Object((1,3,6,1,4,1,37447,1,2,1,1),_VolIndex_Type())
volIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:volIndex.setStatus(_A)
_VolID_Type=Unsigned32
_VolID_Object=MibTableColumn
volID=_VolID_Object((1,3,6,1,4,1,37447,1,2,1,2),_VolID_Type())
volID.setMaxAccess(_B)
if mibBuilder.loadTexts:volID.setStatus(_A)
_VolName_Type=DisplayString
_VolName_Object=MibTableColumn
volName=_VolName_Object((1,3,6,1,4,1,37447,1,2,1,3),_VolName_Type())
volName.setMaxAccess(_B)
if mibBuilder.loadTexts:volName.setStatus(_A)
_VolSizeLow_Type=Unsigned32
_VolSizeLow_Object=MibTableColumn
volSizeLow=_VolSizeLow_Object((1,3,6,1,4,1,37447,1,2,1,4),_VolSizeLow_Type())
volSizeLow.setMaxAccess(_B)
if mibBuilder.loadTexts:volSizeLow.setStatus(_A)
_VolSizeHigh_Type=Unsigned32
_VolSizeHigh_Object=MibTableColumn
volSizeHigh=_VolSizeHigh_Object((1,3,6,1,4,1,37447,1,2,1,5),_VolSizeHigh_Type())
volSizeHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:volSizeHigh.setStatus(_A)
_VolUsageLow_Type=Unsigned32
_VolUsageLow_Object=MibTableColumn
volUsageLow=_VolUsageLow_Object((1,3,6,1,4,1,37447,1,2,1,6),_VolUsageLow_Type())
volUsageLow.setMaxAccess(_B)
if mibBuilder.loadTexts:volUsageLow.setStatus(_A)
_VolUsageHigh_Type=Unsigned32
_VolUsageHigh_Object=MibTableColumn
volUsageHigh=_VolUsageHigh_Object((1,3,6,1,4,1,37447,1,2,1,7),_VolUsageHigh_Type())
volUsageHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:volUsageHigh.setStatus(_A)
_VolReserveLow_Type=Unsigned32
_VolReserveLow_Object=MibTableColumn
volReserveLow=_VolReserveLow_Object((1,3,6,1,4,1,37447,1,2,1,8),_VolReserveLow_Type())
volReserveLow.setMaxAccess(_B)
if mibBuilder.loadTexts:volReserveLow.setStatus(_A)
_VolReserveHigh_Type=Unsigned32
_VolReserveHigh_Object=MibTableColumn
volReserveHigh=_VolReserveHigh_Object((1,3,6,1,4,1,37447,1,2,1,9),_VolReserveHigh_Type())
volReserveHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:volReserveHigh.setStatus(_A)
_VolOnline_Type=TruthValue
_VolOnline_Object=MibTableColumn
volOnline=_VolOnline_Object((1,3,6,1,4,1,37447,1,2,1,10),_VolOnline_Type())
volOnline.setMaxAccess(_B)
if mibBuilder.loadTexts:volOnline.setStatus(_A)
_VolNumConnections_Type=Unsigned32
_VolNumConnections_Object=MibTableColumn
volNumConnections=_VolNumConnections_Object((1,3,6,1,4,1,37447,1,2,1,11),_VolNumConnections_Type())
volNumConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:volNumConnections.setStatus(_A)
_VolStatTimeEpochSeconds_Type=Counter64
_VolStatTimeEpochSeconds_Object=MibTableColumn
volStatTimeEpochSeconds=_VolStatTimeEpochSeconds_Object((1,3,6,1,4,1,37447,1,2,1,12),_VolStatTimeEpochSeconds_Type())
volStatTimeEpochSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:volStatTimeEpochSeconds.setStatus(_A)
_VolIoReads_Type=Counter64
_VolIoReads_Object=MibTableColumn
volIoReads=_VolIoReads_Object((1,3,6,1,4,1,37447,1,2,1,13),_VolIoReads_Type())
volIoReads.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReads.setStatus(_A)
_VolIoReadTimeMicrosec_Type=Counter64
_VolIoReadTimeMicrosec_Object=MibTableColumn
volIoReadTimeMicrosec=_VolIoReadTimeMicrosec_Object((1,3,6,1,4,1,37447,1,2,1,14),_VolIoReadTimeMicrosec_Type())
volIoReadTimeMicrosec.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadTimeMicrosec.setStatus(_A)
_VolIoReadBytes_Type=Counter64
_VolIoReadBytes_Object=MibTableColumn
volIoReadBytes=_VolIoReadBytes_Object((1,3,6,1,4,1,37447,1,2,1,15),_VolIoReadBytes_Type())
volIoReadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadBytes.setStatus(_A)
_VolIoSeqReads_Type=Counter64
_VolIoSeqReads_Object=MibTableColumn
volIoSeqReads=_VolIoSeqReads_Object((1,3,6,1,4,1,37447,1,2,1,16),_VolIoSeqReads_Type())
volIoSeqReads.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoSeqReads.setStatus(_A)
_VolIoSeqReadBytes_Type=Counter64
_VolIoSeqReadBytes_Object=MibTableColumn
volIoSeqReadBytes=_VolIoSeqReadBytes_Object((1,3,6,1,4,1,37447,1,2,1,17),_VolIoSeqReadBytes_Type())
volIoSeqReadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoSeqReadBytes.setStatus(_A)
_VolIoNonseqReadTotalHits_Type=Counter64
_VolIoNonseqReadTotalHits_Object=MibTableColumn
volIoNonseqReadTotalHits=_VolIoNonseqReadTotalHits_Object((1,3,6,1,4,1,37447,1,2,1,18),_VolIoNonseqReadTotalHits_Type())
volIoNonseqReadTotalHits.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoNonseqReadTotalHits.setStatus(_A)
_VolIoNonseqReadMemHits_Type=Counter64
_VolIoNonseqReadMemHits_Object=MibTableColumn
volIoNonseqReadMemHits=_VolIoNonseqReadMemHits_Object((1,3,6,1,4,1,37447,1,2,1,19),_VolIoNonseqReadMemHits_Type())
volIoNonseqReadMemHits.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoNonseqReadMemHits.setStatus(_A)
_VolIoNonseqReadSSDHits_Type=Counter64
_VolIoNonseqReadSSDHits_Object=MibTableColumn
volIoNonseqReadSSDHits=_VolIoNonseqReadSSDHits_Object((1,3,6,1,4,1,37447,1,2,1,20),_VolIoNonseqReadSSDHits_Type())
volIoNonseqReadSSDHits.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoNonseqReadSSDHits.setStatus(_A)
_VolIoReadLatency0uTo100u_Type=Counter64
_VolIoReadLatency0uTo100u_Object=MibTableColumn
volIoReadLatency0uTo100u=_VolIoReadLatency0uTo100u_Object((1,3,6,1,4,1,37447,1,2,1,21),_VolIoReadLatency0uTo100u_Type())
volIoReadLatency0uTo100u.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency0uTo100u.setStatus(_A)
_VolIoReadLatency100uTo200u_Type=Counter64
_VolIoReadLatency100uTo200u_Object=MibTableColumn
volIoReadLatency100uTo200u=_VolIoReadLatency100uTo200u_Object((1,3,6,1,4,1,37447,1,2,1,22),_VolIoReadLatency100uTo200u_Type())
volIoReadLatency100uTo200u.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency100uTo200u.setStatus(_A)
_VolIoReadLatency200uTo500u_Type=Counter64
_VolIoReadLatency200uTo500u_Object=MibTableColumn
volIoReadLatency200uTo500u=_VolIoReadLatency200uTo500u_Object((1,3,6,1,4,1,37447,1,2,1,23),_VolIoReadLatency200uTo500u_Type())
volIoReadLatency200uTo500u.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency200uTo500u.setStatus(_A)
_VolIoReadLatency500uTo1m_Type=Counter64
_VolIoReadLatency500uTo1m_Object=MibTableColumn
volIoReadLatency500uTo1m=_VolIoReadLatency500uTo1m_Object((1,3,6,1,4,1,37447,1,2,1,24),_VolIoReadLatency500uTo1m_Type())
volIoReadLatency500uTo1m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency500uTo1m.setStatus(_A)
_VolIoReadLatency1mTo2m_Type=Counter64
_VolIoReadLatency1mTo2m_Object=MibTableColumn
volIoReadLatency1mTo2m=_VolIoReadLatency1mTo2m_Object((1,3,6,1,4,1,37447,1,2,1,25),_VolIoReadLatency1mTo2m_Type())
volIoReadLatency1mTo2m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency1mTo2m.setStatus(_A)
_VolIoReadLatency2mTo5m_Type=Counter64
_VolIoReadLatency2mTo5m_Object=MibTableColumn
volIoReadLatency2mTo5m=_VolIoReadLatency2mTo5m_Object((1,3,6,1,4,1,37447,1,2,1,26),_VolIoReadLatency2mTo5m_Type())
volIoReadLatency2mTo5m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency2mTo5m.setStatus(_A)
_VolIoReadLatency5mTo10m_Type=Counter64
_VolIoReadLatency5mTo10m_Object=MibTableColumn
volIoReadLatency5mTo10m=_VolIoReadLatency5mTo10m_Object((1,3,6,1,4,1,37447,1,2,1,27),_VolIoReadLatency5mTo10m_Type())
volIoReadLatency5mTo10m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency5mTo10m.setStatus(_A)
_VolIoReadLatency10mTo20m_Type=Counter64
_VolIoReadLatency10mTo20m_Object=MibTableColumn
volIoReadLatency10mTo20m=_VolIoReadLatency10mTo20m_Object((1,3,6,1,4,1,37447,1,2,1,28),_VolIoReadLatency10mTo20m_Type())
volIoReadLatency10mTo20m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency10mTo20m.setStatus(_A)
_VolIoReadLatency20mTo50m_Type=Counter64
_VolIoReadLatency20mTo50m_Object=MibTableColumn
volIoReadLatency20mTo50m=_VolIoReadLatency20mTo50m_Object((1,3,6,1,4,1,37447,1,2,1,29),_VolIoReadLatency20mTo50m_Type())
volIoReadLatency20mTo50m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency20mTo50m.setStatus(_A)
_VolIoReadLatency50mTo100m_Type=Counter64
_VolIoReadLatency50mTo100m_Object=MibTableColumn
volIoReadLatency50mTo100m=_VolIoReadLatency50mTo100m_Object((1,3,6,1,4,1,37447,1,2,1,30),_VolIoReadLatency50mTo100m_Type())
volIoReadLatency50mTo100m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency50mTo100m.setStatus(_A)
_VolIoReadLatency100mTo200m_Type=Counter64
_VolIoReadLatency100mTo200m_Object=MibTableColumn
volIoReadLatency100mTo200m=_VolIoReadLatency100mTo200m_Object((1,3,6,1,4,1,37447,1,2,1,31),_VolIoReadLatency100mTo200m_Type())
volIoReadLatency100mTo200m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency100mTo200m.setStatus(_A)
_VolIoReadLatency200mTo500m_Type=Counter64
_VolIoReadLatency200mTo500m_Object=MibTableColumn
volIoReadLatency200mTo500m=_VolIoReadLatency200mTo500m_Object((1,3,6,1,4,1,37447,1,2,1,32),_VolIoReadLatency200mTo500m_Type())
volIoReadLatency200mTo500m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency200mTo500m.setStatus(_A)
_VolIoReadLatency500mTomax_Type=Counter64
_VolIoReadLatency500mTomax_Object=MibTableColumn
volIoReadLatency500mTomax=_VolIoReadLatency500mTomax_Object((1,3,6,1,4,1,37447,1,2,1,33),_VolIoReadLatency500mTomax_Type())
volIoReadLatency500mTomax.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoReadLatency500mTomax.setStatus(_A)
_VolIoWrites_Type=Counter64
_VolIoWrites_Object=MibTableColumn
volIoWrites=_VolIoWrites_Object((1,3,6,1,4,1,37447,1,2,1,34),_VolIoWrites_Type())
volIoWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWrites.setStatus(_A)
_VolIoWriteTimeMicrosec_Type=Counter64
_VolIoWriteTimeMicrosec_Object=MibTableColumn
volIoWriteTimeMicrosec=_VolIoWriteTimeMicrosec_Object((1,3,6,1,4,1,37447,1,2,1,35),_VolIoWriteTimeMicrosec_Type())
volIoWriteTimeMicrosec.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteTimeMicrosec.setStatus(_A)
_VolIoWriteBytes_Type=Counter64
_VolIoWriteBytes_Object=MibTableColumn
volIoWriteBytes=_VolIoWriteBytes_Object((1,3,6,1,4,1,37447,1,2,1,36),_VolIoWriteBytes_Type())
volIoWriteBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteBytes.setStatus(_A)
_VolIoSeqWrites_Type=Counter64
_VolIoSeqWrites_Object=MibTableColumn
volIoSeqWrites=_VolIoSeqWrites_Object((1,3,6,1,4,1,37447,1,2,1,37),_VolIoSeqWrites_Type())
volIoSeqWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoSeqWrites.setStatus(_A)
_VolIoSeqWriteBytes_Type=Counter64
_VolIoSeqWriteBytes_Object=MibTableColumn
volIoSeqWriteBytes=_VolIoSeqWriteBytes_Object((1,3,6,1,4,1,37447,1,2,1,38),_VolIoSeqWriteBytes_Type())
volIoSeqWriteBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoSeqWriteBytes.setStatus(_A)
_VolIoWriteLatency0uTo100u_Type=Counter64
_VolIoWriteLatency0uTo100u_Object=MibTableColumn
volIoWriteLatency0uTo100u=_VolIoWriteLatency0uTo100u_Object((1,3,6,1,4,1,37447,1,2,1,39),_VolIoWriteLatency0uTo100u_Type())
volIoWriteLatency0uTo100u.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency0uTo100u.setStatus(_A)
_VolIoWriteLatency100uTo200u_Type=Counter64
_VolIoWriteLatency100uTo200u_Object=MibTableColumn
volIoWriteLatency100uTo200u=_VolIoWriteLatency100uTo200u_Object((1,3,6,1,4,1,37447,1,2,1,40),_VolIoWriteLatency100uTo200u_Type())
volIoWriteLatency100uTo200u.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency100uTo200u.setStatus(_A)
_VolIoWriteLatency200uTo500u_Type=Counter64
_VolIoWriteLatency200uTo500u_Object=MibTableColumn
volIoWriteLatency200uTo500u=_VolIoWriteLatency200uTo500u_Object((1,3,6,1,4,1,37447,1,2,1,41),_VolIoWriteLatency200uTo500u_Type())
volIoWriteLatency200uTo500u.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency200uTo500u.setStatus(_A)
_VolIoWriteLatency500uTo1m_Type=Counter64
_VolIoWriteLatency500uTo1m_Object=MibTableColumn
volIoWriteLatency500uTo1m=_VolIoWriteLatency500uTo1m_Object((1,3,6,1,4,1,37447,1,2,1,42),_VolIoWriteLatency500uTo1m_Type())
volIoWriteLatency500uTo1m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency500uTo1m.setStatus(_A)
_VolIoWriteLatency1mTo2m_Type=Counter64
_VolIoWriteLatency1mTo2m_Object=MibTableColumn
volIoWriteLatency1mTo2m=_VolIoWriteLatency1mTo2m_Object((1,3,6,1,4,1,37447,1,2,1,43),_VolIoWriteLatency1mTo2m_Type())
volIoWriteLatency1mTo2m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency1mTo2m.setStatus(_A)
_VolIoWriteLatency2mTo5m_Type=Counter64
_VolIoWriteLatency2mTo5m_Object=MibTableColumn
volIoWriteLatency2mTo5m=_VolIoWriteLatency2mTo5m_Object((1,3,6,1,4,1,37447,1,2,1,44),_VolIoWriteLatency2mTo5m_Type())
volIoWriteLatency2mTo5m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency2mTo5m.setStatus(_A)
_VolIoWriteLatency5mTo10m_Type=Counter64
_VolIoWriteLatency5mTo10m_Object=MibTableColumn
volIoWriteLatency5mTo10m=_VolIoWriteLatency5mTo10m_Object((1,3,6,1,4,1,37447,1,2,1,45),_VolIoWriteLatency5mTo10m_Type())
volIoWriteLatency5mTo10m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency5mTo10m.setStatus(_A)
_VolIoWriteLatency10mTo20m_Type=Counter64
_VolIoWriteLatency10mTo20m_Object=MibTableColumn
volIoWriteLatency10mTo20m=_VolIoWriteLatency10mTo20m_Object((1,3,6,1,4,1,37447,1,2,1,46),_VolIoWriteLatency10mTo20m_Type())
volIoWriteLatency10mTo20m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency10mTo20m.setStatus(_A)
_VolIoWriteLatency20mTo50m_Type=Counter64
_VolIoWriteLatency20mTo50m_Object=MibTableColumn
volIoWriteLatency20mTo50m=_VolIoWriteLatency20mTo50m_Object((1,3,6,1,4,1,37447,1,2,1,47),_VolIoWriteLatency20mTo50m_Type())
volIoWriteLatency20mTo50m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency20mTo50m.setStatus(_A)
_VolIoWriteLatency50mTo100m_Type=Counter64
_VolIoWriteLatency50mTo100m_Object=MibTableColumn
volIoWriteLatency50mTo100m=_VolIoWriteLatency50mTo100m_Object((1,3,6,1,4,1,37447,1,2,1,48),_VolIoWriteLatency50mTo100m_Type())
volIoWriteLatency50mTo100m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency50mTo100m.setStatus(_A)
_VolIoWriteLatency100mTo200m_Type=Counter64
_VolIoWriteLatency100mTo200m_Object=MibTableColumn
volIoWriteLatency100mTo200m=_VolIoWriteLatency100mTo200m_Object((1,3,6,1,4,1,37447,1,2,1,49),_VolIoWriteLatency100mTo200m_Type())
volIoWriteLatency100mTo200m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency100mTo200m.setStatus(_A)
_VolIoWriteLatency200mTo500m_Type=Counter64
_VolIoWriteLatency200mTo500m_Object=MibTableColumn
volIoWriteLatency200mTo500m=_VolIoWriteLatency200mTo500m_Object((1,3,6,1,4,1,37447,1,2,1,50),_VolIoWriteLatency200mTo500m_Type())
volIoWriteLatency200mTo500m.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency200mTo500m.setStatus(_A)
_VolIoWriteLatency500mTomax_Type=Counter64
_VolIoWriteLatency500mTomax_Object=MibTableColumn
volIoWriteLatency500mTomax=_VolIoWriteLatency500mTomax_Object((1,3,6,1,4,1,37447,1,2,1,51),_VolIoWriteLatency500mTomax_Type())
volIoWriteLatency500mTomax.setMaxAccess(_B)
if mibBuilder.loadTexts:volIoWriteLatency500mTomax.setStatus(_A)
_VolDiskVolBytesUsedLow_Type=Unsigned32
_VolDiskVolBytesUsedLow_Object=MibTableColumn
volDiskVolBytesUsedLow=_VolDiskVolBytesUsedLow_Object((1,3,6,1,4,1,37447,1,2,1,52),_VolDiskVolBytesUsedLow_Type())
volDiskVolBytesUsedLow.setMaxAccess(_B)
if mibBuilder.loadTexts:volDiskVolBytesUsedLow.setStatus(_A)
_VolDiskVolBytesUsedHigh_Type=Unsigned32
_VolDiskVolBytesUsedHigh_Object=MibTableColumn
volDiskVolBytesUsedHigh=_VolDiskVolBytesUsedHigh_Object((1,3,6,1,4,1,37447,1,2,1,53),_VolDiskVolBytesUsedHigh_Type())
volDiskVolBytesUsedHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:volDiskVolBytesUsedHigh.setStatus(_A)
_VolDiskSnapBytesUsedLow_Type=Unsigned32
_VolDiskSnapBytesUsedLow_Object=MibTableColumn
volDiskSnapBytesUsedLow=_VolDiskSnapBytesUsedLow_Object((1,3,6,1,4,1,37447,1,2,1,54),_VolDiskSnapBytesUsedLow_Type())
volDiskSnapBytesUsedLow.setMaxAccess(_B)
if mibBuilder.loadTexts:volDiskSnapBytesUsedLow.setStatus(_A)
_VolDiskSnapBytesUsedHigh_Type=Unsigned32
_VolDiskSnapBytesUsedHigh_Object=MibTableColumn
volDiskSnapBytesUsedHigh=_VolDiskSnapBytesUsedHigh_Object((1,3,6,1,4,1,37447,1,2,1,55),_VolDiskSnapBytesUsedHigh_Type())
volDiskSnapBytesUsedHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:volDiskSnapBytesUsedHigh.setStatus(_A)
_GlobalStats_ObjectIdentity=ObjectIdentity
globalStats=_GlobalStats_ObjectIdentity((1,3,6,1,4,1,37447,1,3))
_StatTimeEpochSeconds_Type=Counter64
_StatTimeEpochSeconds_Object=MibScalar
statTimeEpochSeconds=_StatTimeEpochSeconds_Object((1,3,6,1,4,1,37447,1,3,1),_StatTimeEpochSeconds_Type())
statTimeEpochSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:statTimeEpochSeconds.setStatus(_A)
_IoReads_Type=Counter64
_IoReads_Object=MibScalar
ioReads=_IoReads_Object((1,3,6,1,4,1,37447,1,3,2),_IoReads_Type())
ioReads.setMaxAccess(_B)
if mibBuilder.loadTexts:ioReads.setStatus(_A)
_IoSeqReads_Type=Counter64
_IoSeqReads_Object=MibScalar
ioSeqReads=_IoSeqReads_Object((1,3,6,1,4,1,37447,1,3,3),_IoSeqReads_Type())
ioSeqReads.setMaxAccess(_B)
if mibBuilder.loadTexts:ioSeqReads.setStatus(_A)
_IoWrites_Type=Counter64
_IoWrites_Object=MibScalar
ioWrites=_IoWrites_Object((1,3,6,1,4,1,37447,1,3,4),_IoWrites_Type())
ioWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:ioWrites.setStatus(_A)
_IoSeqWrites_Type=Counter64
_IoSeqWrites_Object=MibScalar
ioSeqWrites=_IoSeqWrites_Object((1,3,6,1,4,1,37447,1,3,5),_IoSeqWrites_Type())
ioSeqWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:ioSeqWrites.setStatus(_A)
_IoReadTimeMicrosec_Type=Counter64
_IoReadTimeMicrosec_Object=MibScalar
ioReadTimeMicrosec=_IoReadTimeMicrosec_Object((1,3,6,1,4,1,37447,1,3,6),_IoReadTimeMicrosec_Type())
ioReadTimeMicrosec.setMaxAccess(_B)
if mibBuilder.loadTexts:ioReadTimeMicrosec.setStatus(_A)
_IoWriteTimeMicrosec_Type=Counter64
_IoWriteTimeMicrosec_Object=MibScalar
ioWriteTimeMicrosec=_IoWriteTimeMicrosec_Object((1,3,6,1,4,1,37447,1,3,7),_IoWriteTimeMicrosec_Type())
ioWriteTimeMicrosec.setMaxAccess(_B)
if mibBuilder.loadTexts:ioWriteTimeMicrosec.setStatus(_A)
_IoReadBytes_Type=Counter64
_IoReadBytes_Object=MibScalar
ioReadBytes=_IoReadBytes_Object((1,3,6,1,4,1,37447,1,3,8),_IoReadBytes_Type())
ioReadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ioReadBytes.setStatus(_A)
_IoSeqReadBytes_Type=Counter64
_IoSeqReadBytes_Object=MibScalar
ioSeqReadBytes=_IoSeqReadBytes_Object((1,3,6,1,4,1,37447,1,3,9),_IoSeqReadBytes_Type())
ioSeqReadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ioSeqReadBytes.setStatus(_A)
_IoWriteBytes_Type=Counter64
_IoWriteBytes_Object=MibScalar
ioWriteBytes=_IoWriteBytes_Object((1,3,6,1,4,1,37447,1,3,10),_IoWriteBytes_Type())
ioWriteBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ioWriteBytes.setStatus(_A)
_IoSeqWriteBytes_Type=Counter64
_IoSeqWriteBytes_Object=MibScalar
ioSeqWriteBytes=_IoSeqWriteBytes_Object((1,3,6,1,4,1,37447,1,3,11),_IoSeqWriteBytes_Type())
ioSeqWriteBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ioSeqWriteBytes.setStatus(_A)
_DiskVolBytesUsedLow_Type=Unsigned32
_DiskVolBytesUsedLow_Object=MibScalar
diskVolBytesUsedLow=_DiskVolBytesUsedLow_Object((1,3,6,1,4,1,37447,1,3,12),_DiskVolBytesUsedLow_Type())
diskVolBytesUsedLow.setMaxAccess(_B)
if mibBuilder.loadTexts:diskVolBytesUsedLow.setStatus(_A)
_DiskVolBytesUsedHigh_Type=Unsigned32
_DiskVolBytesUsedHigh_Object=MibScalar
diskVolBytesUsedHigh=_DiskVolBytesUsedHigh_Object((1,3,6,1,4,1,37447,1,3,13),_DiskVolBytesUsedHigh_Type())
diskVolBytesUsedHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:diskVolBytesUsedHigh.setStatus(_A)
_DiskSnapBytesUsedLow_Type=Unsigned32
_DiskSnapBytesUsedLow_Object=MibScalar
diskSnapBytesUsedLow=_DiskSnapBytesUsedLow_Object((1,3,6,1,4,1,37447,1,3,14),_DiskSnapBytesUsedLow_Type())
diskSnapBytesUsedLow.setMaxAccess(_B)
if mibBuilder.loadTexts:diskSnapBytesUsedLow.setStatus(_A)
_DiskSnapBytesUsedHigh_Type=Unsigned32
_DiskSnapBytesUsedHigh_Object=MibScalar
diskSnapBytesUsedHigh=_DiskSnapBytesUsedHigh_Object((1,3,6,1,4,1,37447,1,3,15),_DiskSnapBytesUsedHigh_Type())
diskSnapBytesUsedHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:diskSnapBytesUsedHigh.setStatus(_A)
_IoNonseqReadHits_Type=Counter64
_IoNonseqReadHits_Object=MibScalar
ioNonseqReadHits=_IoNonseqReadHits_Object((1,3,6,1,4,1,37447,1,3,16),_IoNonseqReadHits_Type())
ioNonseqReadHits.setMaxAccess(_B)
if mibBuilder.loadTexts:ioNonseqReadHits.setStatus(_A)
_Arrays_ObjectIdentity=ObjectIdentity
arrays=_Arrays_ObjectIdentity((1,3,6,1,4,1,37447,3))
_ArrayEntry_Type=DisplayString
_ArrayEntry_Object=MibScalar
arrayEntry=_ArrayEntry_Object((1,3,6,1,4,1,37447,3,1),_ArrayEntry_Type())
arrayEntry.setMaxAccess(_E)
if mibBuilder.loadTexts:arrayEntry.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nimble':nimble,'variables':variables,'volNumberOfVolumes':volNumberOfVolumes,'volTable':volTable,'volEntry':volEntry,_D:volIndex,'volID':volID,'volName':volName,'volSizeLow':volSizeLow,'volSizeHigh':volSizeHigh,'volUsageLow':volUsageLow,'volUsageHigh':volUsageHigh,'volReserveLow':volReserveLow,'volReserveHigh':volReserveHigh,'volOnline':volOnline,'volNumConnections':volNumConnections,'volStatTimeEpochSeconds':volStatTimeEpochSeconds,'volIoReads':volIoReads,'volIoReadTimeMicrosec':volIoReadTimeMicrosec,'volIoReadBytes':volIoReadBytes,'volIoSeqReads':volIoSeqReads,'volIoSeqReadBytes':volIoSeqReadBytes,'volIoNonseqReadTotalHits':volIoNonseqReadTotalHits,'volIoNonseqReadMemHits':volIoNonseqReadMemHits,'volIoNonseqReadSSDHits':volIoNonseqReadSSDHits,'volIoReadLatency0uTo100u':volIoReadLatency0uTo100u,'volIoReadLatency100uTo200u':volIoReadLatency100uTo200u,'volIoReadLatency200uTo500u':volIoReadLatency200uTo500u,'volIoReadLatency500uTo1m':volIoReadLatency500uTo1m,'volIoReadLatency1mTo2m':volIoReadLatency1mTo2m,'volIoReadLatency2mTo5m':volIoReadLatency2mTo5m,'volIoReadLatency5mTo10m':volIoReadLatency5mTo10m,'volIoReadLatency10mTo20m':volIoReadLatency10mTo20m,'volIoReadLatency20mTo50m':volIoReadLatency20mTo50m,'volIoReadLatency50mTo100m':volIoReadLatency50mTo100m,'volIoReadLatency100mTo200m':volIoReadLatency100mTo200m,'volIoReadLatency200mTo500m':volIoReadLatency200mTo500m,'volIoReadLatency500mTomax':volIoReadLatency500mTomax,'volIoWrites':volIoWrites,'volIoWriteTimeMicrosec':volIoWriteTimeMicrosec,'volIoWriteBytes':volIoWriteBytes,'volIoSeqWrites':volIoSeqWrites,'volIoSeqWriteBytes':volIoSeqWriteBytes,'volIoWriteLatency0uTo100u':volIoWriteLatency0uTo100u,'volIoWriteLatency100uTo200u':volIoWriteLatency100uTo200u,'volIoWriteLatency200uTo500u':volIoWriteLatency200uTo500u,'volIoWriteLatency500uTo1m':volIoWriteLatency500uTo1m,'volIoWriteLatency1mTo2m':volIoWriteLatency1mTo2m,'volIoWriteLatency2mTo5m':volIoWriteLatency2mTo5m,'volIoWriteLatency5mTo10m':volIoWriteLatency5mTo10m,'volIoWriteLatency10mTo20m':volIoWriteLatency10mTo20m,'volIoWriteLatency20mTo50m':volIoWriteLatency20mTo50m,'volIoWriteLatency50mTo100m':volIoWriteLatency50mTo100m,'volIoWriteLatency100mTo200m':volIoWriteLatency100mTo200m,'volIoWriteLatency200mTo500m':volIoWriteLatency200mTo500m,'volIoWriteLatency500mTomax':volIoWriteLatency500mTomax,'volDiskVolBytesUsedLow':volDiskVolBytesUsedLow,'volDiskVolBytesUsedHigh':volDiskVolBytesUsedHigh,'volDiskSnapBytesUsedLow':volDiskSnapBytesUsedLow,'volDiskSnapBytesUsedHigh':volDiskSnapBytesUsedHigh,'globalStats':globalStats,'statTimeEpochSeconds':statTimeEpochSeconds,'ioReads':ioReads,'ioSeqReads':ioSeqReads,'ioWrites':ioWrites,'ioSeqWrites':ioSeqWrites,'ioReadTimeMicrosec':ioReadTimeMicrosec,'ioWriteTimeMicrosec':ioWriteTimeMicrosec,'ioReadBytes':ioReadBytes,'ioSeqReadBytes':ioSeqReadBytes,'ioWriteBytes':ioWriteBytes,'ioSeqWriteBytes':ioSeqWriteBytes,'diskVolBytesUsedLow':diskVolBytesUsedLow,'diskVolBytesUsedHigh':diskVolBytesUsedHigh,'diskSnapBytesUsedLow':diskSnapBytesUsedLow,'diskSnapBytesUsedHigh':diskSnapBytesUsedHigh,'ioNonseqReadHits':ioNonseqReadHits,'arrays':arrays,'arrayEntry':arrayEntry})