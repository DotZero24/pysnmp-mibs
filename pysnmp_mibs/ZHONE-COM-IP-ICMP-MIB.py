_D='zhoneIcmpEntry'
_C='ZHONE-COM-IP-ICMP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdEntry,=mibBuilder.importSymbols('ZHONE-COM-IP-RD-MIB','rdEntry')
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
comIpIcmp=ModuleIdentity((1,3,6,1,4,1,5504,6,55))
if mibBuilder.loadTexts:comIpIcmp.setRevisions(('2000-09-11 16:25',))
_Icmp_ObjectIdentity=ObjectIdentity
icmp=_Icmp_ObjectIdentity((1,3,6,1,4,1,5504,4,1,5))
if mibBuilder.loadTexts:icmp.setStatus(_A)
_ZhoneIcmpTable_Object=MibTable
zhoneIcmpTable=_ZhoneIcmpTable_Object((1,3,6,1,4,1,5504,4,1,5,1))
if mibBuilder.loadTexts:zhoneIcmpTable.setStatus(_A)
_ZhoneIcmpEntry_Object=MibTableRow
zhoneIcmpEntry=_ZhoneIcmpEntry_Object((1,3,6,1,4,1,5504,4,1,5,1,1))
if mibBuilder.loadTexts:zhoneIcmpEntry.setStatus(_A)
_ZhIcmpInMsgs_Type=Counter32
_ZhIcmpInMsgs_Object=MibTableColumn
zhIcmpInMsgs=_ZhIcmpInMsgs_Object((1,3,6,1,4,1,5504,4,1,5,1,1,1),_ZhIcmpInMsgs_Type())
zhIcmpInMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInMsgs.setStatus(_A)
_ZhIcmpInErrors_Type=Counter32
_ZhIcmpInErrors_Object=MibTableColumn
zhIcmpInErrors=_ZhIcmpInErrors_Object((1,3,6,1,4,1,5504,4,1,5,1,1,2),_ZhIcmpInErrors_Type())
zhIcmpInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInErrors.setStatus(_A)
_ZhIcmpInDestUnreachs_Type=Counter32
_ZhIcmpInDestUnreachs_Object=MibTableColumn
zhIcmpInDestUnreachs=_ZhIcmpInDestUnreachs_Object((1,3,6,1,4,1,5504,4,1,5,1,1,3),_ZhIcmpInDestUnreachs_Type())
zhIcmpInDestUnreachs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInDestUnreachs.setStatus(_A)
_ZhIcmpInTimeExcds_Type=Counter32
_ZhIcmpInTimeExcds_Object=MibTableColumn
zhIcmpInTimeExcds=_ZhIcmpInTimeExcds_Object((1,3,6,1,4,1,5504,4,1,5,1,1,4),_ZhIcmpInTimeExcds_Type())
zhIcmpInTimeExcds.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInTimeExcds.setStatus(_A)
_ZhIcmpInParmProbs_Type=Counter32
_ZhIcmpInParmProbs_Object=MibTableColumn
zhIcmpInParmProbs=_ZhIcmpInParmProbs_Object((1,3,6,1,4,1,5504,4,1,5,1,1,5),_ZhIcmpInParmProbs_Type())
zhIcmpInParmProbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInParmProbs.setStatus(_A)
_ZhIcmpInSrcQuenchs_Type=Counter32
_ZhIcmpInSrcQuenchs_Object=MibTableColumn
zhIcmpInSrcQuenchs=_ZhIcmpInSrcQuenchs_Object((1,3,6,1,4,1,5504,4,1,5,1,1,6),_ZhIcmpInSrcQuenchs_Type())
zhIcmpInSrcQuenchs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInSrcQuenchs.setStatus(_A)
_ZhIcmpInRedirects_Type=Counter32
_ZhIcmpInRedirects_Object=MibTableColumn
zhIcmpInRedirects=_ZhIcmpInRedirects_Object((1,3,6,1,4,1,5504,4,1,5,1,1,7),_ZhIcmpInRedirects_Type())
zhIcmpInRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInRedirects.setStatus(_A)
_ZhIcmpInEchos_Type=Counter32
_ZhIcmpInEchos_Object=MibTableColumn
zhIcmpInEchos=_ZhIcmpInEchos_Object((1,3,6,1,4,1,5504,4,1,5,1,1,8),_ZhIcmpInEchos_Type())
zhIcmpInEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInEchos.setStatus(_A)
_ZhIcmpInEchoReps_Type=Counter32
_ZhIcmpInEchoReps_Object=MibTableColumn
zhIcmpInEchoReps=_ZhIcmpInEchoReps_Object((1,3,6,1,4,1,5504,4,1,5,1,1,9),_ZhIcmpInEchoReps_Type())
zhIcmpInEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInEchoReps.setStatus(_A)
_ZhIcmpInTimestamps_Type=Counter32
_ZhIcmpInTimestamps_Object=MibTableColumn
zhIcmpInTimestamps=_ZhIcmpInTimestamps_Object((1,3,6,1,4,1,5504,4,1,5,1,1,10),_ZhIcmpInTimestamps_Type())
zhIcmpInTimestamps.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInTimestamps.setStatus(_A)
_ZhIcmpInTimestampReps_Type=Counter32
_ZhIcmpInTimestampReps_Object=MibTableColumn
zhIcmpInTimestampReps=_ZhIcmpInTimestampReps_Object((1,3,6,1,4,1,5504,4,1,5,1,1,11),_ZhIcmpInTimestampReps_Type())
zhIcmpInTimestampReps.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInTimestampReps.setStatus(_A)
_ZhIcmpInAddrMasks_Type=Counter32
_ZhIcmpInAddrMasks_Object=MibTableColumn
zhIcmpInAddrMasks=_ZhIcmpInAddrMasks_Object((1,3,6,1,4,1,5504,4,1,5,1,1,12),_ZhIcmpInAddrMasks_Type())
zhIcmpInAddrMasks.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInAddrMasks.setStatus(_A)
_ZhIcmpInAddrMaskReps_Type=Counter32
_ZhIcmpInAddrMaskReps_Object=MibTableColumn
zhIcmpInAddrMaskReps=_ZhIcmpInAddrMaskReps_Object((1,3,6,1,4,1,5504,4,1,5,1,1,13),_ZhIcmpInAddrMaskReps_Type())
zhIcmpInAddrMaskReps.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpInAddrMaskReps.setStatus(_A)
_ZhIcmpOutMsgs_Type=Counter32
_ZhIcmpOutMsgs_Object=MibTableColumn
zhIcmpOutMsgs=_ZhIcmpOutMsgs_Object((1,3,6,1,4,1,5504,4,1,5,1,1,14),_ZhIcmpOutMsgs_Type())
zhIcmpOutMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutMsgs.setStatus(_A)
_ZhIcmpOutErrors_Type=Counter32
_ZhIcmpOutErrors_Object=MibTableColumn
zhIcmpOutErrors=_ZhIcmpOutErrors_Object((1,3,6,1,4,1,5504,4,1,5,1,1,15),_ZhIcmpOutErrors_Type())
zhIcmpOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutErrors.setStatus(_A)
_ZhIcmpOutDestUnreachs_Type=Counter32
_ZhIcmpOutDestUnreachs_Object=MibTableColumn
zhIcmpOutDestUnreachs=_ZhIcmpOutDestUnreachs_Object((1,3,6,1,4,1,5504,4,1,5,1,1,16),_ZhIcmpOutDestUnreachs_Type())
zhIcmpOutDestUnreachs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutDestUnreachs.setStatus(_A)
_ZhIcmpOutTimeExcds_Type=Counter32
_ZhIcmpOutTimeExcds_Object=MibTableColumn
zhIcmpOutTimeExcds=_ZhIcmpOutTimeExcds_Object((1,3,6,1,4,1,5504,4,1,5,1,1,17),_ZhIcmpOutTimeExcds_Type())
zhIcmpOutTimeExcds.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutTimeExcds.setStatus(_A)
_ZhIcmpOutParmProbs_Type=Counter32
_ZhIcmpOutParmProbs_Object=MibTableColumn
zhIcmpOutParmProbs=_ZhIcmpOutParmProbs_Object((1,3,6,1,4,1,5504,4,1,5,1,1,18),_ZhIcmpOutParmProbs_Type())
zhIcmpOutParmProbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutParmProbs.setStatus(_A)
_ZhIcmpOutSrcQuenchs_Type=Counter32
_ZhIcmpOutSrcQuenchs_Object=MibTableColumn
zhIcmpOutSrcQuenchs=_ZhIcmpOutSrcQuenchs_Object((1,3,6,1,4,1,5504,4,1,5,1,1,19),_ZhIcmpOutSrcQuenchs_Type())
zhIcmpOutSrcQuenchs.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutSrcQuenchs.setStatus(_A)
_ZhIcmpOutRedirects_Type=Counter32
_ZhIcmpOutRedirects_Object=MibTableColumn
zhIcmpOutRedirects=_ZhIcmpOutRedirects_Object((1,3,6,1,4,1,5504,4,1,5,1,1,20),_ZhIcmpOutRedirects_Type())
zhIcmpOutRedirects.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutRedirects.setStatus(_A)
_ZhIcmpOutEchos_Type=Counter32
_ZhIcmpOutEchos_Object=MibTableColumn
zhIcmpOutEchos=_ZhIcmpOutEchos_Object((1,3,6,1,4,1,5504,4,1,5,1,1,21),_ZhIcmpOutEchos_Type())
zhIcmpOutEchos.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutEchos.setStatus(_A)
_ZhIcmpOutEchoReps_Type=Counter32
_ZhIcmpOutEchoReps_Object=MibTableColumn
zhIcmpOutEchoReps=_ZhIcmpOutEchoReps_Object((1,3,6,1,4,1,5504,4,1,5,1,1,22),_ZhIcmpOutEchoReps_Type())
zhIcmpOutEchoReps.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutEchoReps.setStatus(_A)
_ZhIcmpOutTimestamps_Type=Counter32
_ZhIcmpOutTimestamps_Object=MibTableColumn
zhIcmpOutTimestamps=_ZhIcmpOutTimestamps_Object((1,3,6,1,4,1,5504,4,1,5,1,1,23),_ZhIcmpOutTimestamps_Type())
zhIcmpOutTimestamps.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutTimestamps.setStatus(_A)
_ZhIcmpOutTimestampReps_Type=Counter32
_ZhIcmpOutTimestampReps_Object=MibTableColumn
zhIcmpOutTimestampReps=_ZhIcmpOutTimestampReps_Object((1,3,6,1,4,1,5504,4,1,5,1,1,24),_ZhIcmpOutTimestampReps_Type())
zhIcmpOutTimestampReps.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutTimestampReps.setStatus(_A)
_ZhIcmpOutAddrMasks_Type=Counter32
_ZhIcmpOutAddrMasks_Object=MibTableColumn
zhIcmpOutAddrMasks=_ZhIcmpOutAddrMasks_Object((1,3,6,1,4,1,5504,4,1,5,1,1,25),_ZhIcmpOutAddrMasks_Type())
zhIcmpOutAddrMasks.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutAddrMasks.setStatus(_A)
_ZhIcmpOutAddrMaskReps_Type=Counter32
_ZhIcmpOutAddrMaskReps_Object=MibTableColumn
zhIcmpOutAddrMaskReps=_ZhIcmpOutAddrMaskReps_Object((1,3,6,1,4,1,5504,4,1,5,1,1,26),_ZhIcmpOutAddrMaskReps_Type())
zhIcmpOutAddrMaskReps.setMaxAccess(_B)
if mibBuilder.loadTexts:zhIcmpOutAddrMaskReps.setStatus(_A)
rdEntry.registerAugmentions((_C,_D))
zhoneIcmpEntry.setIndexNames(*rdEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'icmp':icmp,'zhoneIcmpTable':zhoneIcmpTable,_D:zhoneIcmpEntry,'zhIcmpInMsgs':zhIcmpInMsgs,'zhIcmpInErrors':zhIcmpInErrors,'zhIcmpInDestUnreachs':zhIcmpInDestUnreachs,'zhIcmpInTimeExcds':zhIcmpInTimeExcds,'zhIcmpInParmProbs':zhIcmpInParmProbs,'zhIcmpInSrcQuenchs':zhIcmpInSrcQuenchs,'zhIcmpInRedirects':zhIcmpInRedirects,'zhIcmpInEchos':zhIcmpInEchos,'zhIcmpInEchoReps':zhIcmpInEchoReps,'zhIcmpInTimestamps':zhIcmpInTimestamps,'zhIcmpInTimestampReps':zhIcmpInTimestampReps,'zhIcmpInAddrMasks':zhIcmpInAddrMasks,'zhIcmpInAddrMaskReps':zhIcmpInAddrMaskReps,'zhIcmpOutMsgs':zhIcmpOutMsgs,'zhIcmpOutErrors':zhIcmpOutErrors,'zhIcmpOutDestUnreachs':zhIcmpOutDestUnreachs,'zhIcmpOutTimeExcds':zhIcmpOutTimeExcds,'zhIcmpOutParmProbs':zhIcmpOutParmProbs,'zhIcmpOutSrcQuenchs':zhIcmpOutSrcQuenchs,'zhIcmpOutRedirects':zhIcmpOutRedirects,'zhIcmpOutEchos':zhIcmpOutEchos,'zhIcmpOutEchoReps':zhIcmpOutEchoReps,'zhIcmpOutTimestamps':zhIcmpOutTimestamps,'zhIcmpOutTimestampReps':zhIcmpOutTimestampReps,'zhIcmpOutAddrMasks':zhIcmpOutAddrMasks,'zhIcmpOutAddrMaskReps':zhIcmpOutAddrMaskReps,'comIpIcmp':comIpIcmp})